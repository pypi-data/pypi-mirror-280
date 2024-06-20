import os
import PyPDF2
import google.generativeai as genai
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings,
    HarmBlockThreshold,
    HarmCategory,
)
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.docstore.document import Document
import json

from insuant.services.insuant.prompt_parameters import PromptService


class GoogleService:

    def __init__(self):
        # todo: add logic to initialize google api
        # Load environment variables from .env file
        load_dotenv()
        os.environ["LANGCHAIN_TRACING_V2"] = "true"
        os.environ["LANGCHAIN_PROJECT"] = "AI-SaaS"
        os.environ["LANGCHAIN_API_KEY"] = os.getenv('LANGCHAIN_API_KEY')
        self.ps = PromptService()
        # Configure Google API with API key from .env file
        genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

    # Generate summaries of text elements
    def generate_text_summaries(self, texts, tables, summarize_texts=False):
        """
        Summarize text elements
        texts: List of str
        tables: List of str
        summarize_texts: Bool to summarize texts
        """

        # Prompt
        # old 
        # prompt_text = """"You are contract Management analyst with key role is to legal validation of contracts and amendments. \
        # You are tasked with summarizing tables and text for retrieval. \
        # These summaries will be embedded and used to retrieve the raw text or table elements. \
        # Give a concise summary of the table or text that is well optimized for retrieval. Table or text: {element} \
        # new
        prompt_text = self.ps.getConfig('generate_text_summaries_prompt')
        # provide the output in a Json format."""

        all_texts = "[ "
        all_tables = ". "
        for text in texts:
            all_texts += text
        for table in tables:
            all_tables += table
        prompt_text += all_texts
        prompt_text += all_tables
        prompt_text += "]"

        # print("prompt_text: ", prompt_text)

        prompt = ChatPromptTemplate.from_template(prompt_text)

        # Text summary chain
        model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.1)
        summarize_chain = {"element": lambda x: x} | prompt | model | StrOutputParser()

        # Initialize empty summaries
        text_summaries = []
        table_summaries = []

        # Apply to text if texts are provided and summarization is requested
        if texts and summarize_texts:
            text_summaries = summarize_chain.batch(texts, {"max_concurrency": 5})
        elif texts:
            text_summaries = texts

        # print("text_summaries: ", text_summaries)

        # Apply to tables if tables are provided
        if tables:
            table_summaries = summarize_chain.batch(tables, {"max_concurrency": 5})
        # print("table_summaries: ", table_summaries)
        # print("text_summaries: ", json.loads(text_summaries[0]))

        self.get_vector_store(text_summaries)

        return text_summaries, table_summaries

    def get_vector_store(self, chunks):
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001")  # type: ignore
        vector_store = FAISS.from_texts(chunks, embedding=embeddings)
        vector_store.save_local("faiss_index")

        if os.path.exists('../../faiss_index'):
            print("inside existing: ")
            vector_store = FAISS.load_local("faiss_index", embeddings)
            vector_store.from_texts(chunks, embedding=embeddings)
        else:
            print("inside new: ")
            vector_store = FAISS.from_texts(chunks, embedding=embeddings)
            vector_store.save_local("faiss_index")

        # Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
        ##provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
        # Context:\n {context}?\n
        # Question: \n{question}\n

    def get_conversational_chain(self, prompt_template):

        model = ChatGoogleGenerativeAI(model="gemini-pro",
                                       client=genai,
                                       temperature=0.3,
                                       safety_settings={
                                           HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
                                           HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                                           HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
                                           HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                                           # HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
                                       },
                                       )

        prompt = PromptTemplate(template=prompt_template,
                                input_variables=["context", "question"],
                                validate_template=False, template_format="f-string",
                                )
        chain = load_qa_chain(llm=model, chain_type="stuff", prompt=prompt)
        return chain

    def user_input(self, user_question, prompt_template):
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001")  # type: ignore

        new_db = FAISS.load_local("faiss_index", embeddings)
        docs = new_db.similarity_search(user_question)

        chain = self.get_conversational_chain(prompt_template)
        # print("docs: ", docs)

        response = chain.invoke(
            {"input_documents": docs, "question": user_question, "context": docs},
            return_only_outputs=False, )

        # print(response)
        return response

    def user_input_nofaiss(self, prompt_text, user_question, history, docs):

        chain = self.get_conversational_chain(prompt_text)
        print("chain: ", chain)

        response = chain.invoke(
            {"input_documents": docs, "question": user_question, "context": docs, "history": history},
            return_only_outputs=False, )

        # print(response)
        return response

    def get_data(self, page_content):
        _dict = {}
        page_content_list = page_content.splitlines()
        for line in page_content_list:
            if ':' not in line:
                continue
            key, value = line.split(':')
            _dict[key.strip()] = value.strip()
        return _dict

    def get_document_obj(self, page_content):
        return Document(page_content=page_content)

    # Open the PDF file
    def extract_pdf_content(self, fname):
        # Open the PDF file
        pdf_file = PyPDF2.PdfReader(fname)

        # Extract the content from each page
        content = []
        for page in pdf_file.pages:
            content.append(page.extract_text())

        # Convert the content to JSON format
        json_content = json.dumps(content)

        return json_content

    # Generate summaries of text elements
    def chat_with_docs(self, question, context, history):

        # new
        prompt_text = """
        You are a Sales executive who manages and reviews Contract Management docuements and business profits. 
        You are tasked with answering the below user Question related to the contract documents summaries 
        provided on the Text Context. last 3 chat history is also provided for your reference. 
        Don't be afraid to ask for more details if needed. \n\n
                    
        Text Context:\n {context}\n

        Chat History:\n {history}?\n

        Question:\n {question}?\n

        Answer: """

        prompt_text = """
            Dear Sales Executive, entrusted with managing and evaluating Contract Management documents and business profitability,
            You are now presented with a user question related to the single contract documents provided in the Text Context. 
            Take into account the last three chat interactions for context and feel free to request additional details if necessary.
            if you cont't find the answer in the provided context, just say, "answer is not available in the document" and respond 
            how its generally handle in contract management industry.

            Text Context:
            {context}

            Chat History:
            {history}?

            User Question:
            {question}?

            Your Answer:
        """

        prompt_text = self.ps.getConfig('chat_with_docs_prompt')
        prompt_text.format(context=context, history=history, question=question)

        # prompt_template = ChatPromptTemplate.from_template(prompt_text)

        # print ("prompt_template: ", prompt_template)

        # response = self.user_input(question, prompt_text)

        response = self.user_input_nofaiss(prompt_text=prompt_text, user_question=question, history=history,
                                           docs=context)

        print("response: ", response["output_text"])

        return response["output_text"]

    # Generate summaries of text elements
    def chat_with_single_doc(self, question, context, history):

        # new
        prompt_text = """
        System:\n You are a Sales executive who manages and reviews Contract Management docuements and business profits. 
        You are tasked with answering the below user Question related to the contract documents summaries 
        provided on the Text Context. last 3 chat history is also provided for your reference. 
        Don't be afraid to ask for more details if needed. \n\n
                    
        Text Context:\n {context}\n

        History:\n {history}?\n

        Question:\n {question}?\n

        Answer: """

        prompt_text = """
            Dear Sales Executive, entrusted with managing and evaluating Contract Management documents and business profitability,
            You are now presented with a user question related to the multiple contract documents provided in the Text Context. 
            Take into account the last three chat interactions for context and feel free to request additional details if necessary.
            if you cont't find the answer in the provided context, just say, "answer is not available in the document" and respond how its generally handle in contract management industry.

            Text Context:
            {context}

            Chat History:
            {history}?

            User Question:
            {question}?

            Your Answer:
        """

        prompt_text = self.ps.getConfig('chat_with_single_doc_prompt')
        prompt_text.format(context=context, history=history, question=question)

        response = self.user_input_nofaiss(prompt_text=prompt_text, user_question=question, history=history,
                                           docs=context)

        print("response: ", response["output_text"])

        return response["output_text"]

    def db_schema_str(self):
        return """[('table_name': 'mongodb.airandb.listing_air_and_b', 'table_columns': [['_id', 'varchar', '', ''], ['listing_url', 'varchar', '', ''], ['name', 'varchar', '', ''], ['summary', 'varchar', '', ''], ['space', 'varchar', '', ''], ['description', 'varchar', '', ''], ['neighborhood_overview', 'varchar', '', ''], ['notes', 'varchar', '', ''], ['transit', 'varchar', '', ''], ['access', 'varchar', '', ''], ['interaction', 'varchar', '', ''], ['house_rules', 'varchar', '', ''], ['property_type', 'varchar', '', ''], ['room_type', 'varchar', '', ''], ['bed_type', 'varchar', '', ''], ['minimum_nights', 'varchar', '', ''], ['maximum_nights', 'varchar', '', ''], ['cancellation_policy', 'varchar', '', ''], ['last_scraped', 'timestamp', '', ''], ['calendar_last_scraped', 'timestamp', '', ''], ['first_review', 'timestamp', '', ''], ['last_review', 'timestamp', '', ''], ['accommodates', 'bigint', '', ''], ['bedrooms', 'bigint', '', ''], ['beds', 'bigint', '', ''], ['number_of_reviews', 'bigint', '', ''], ['amenities', 'array(varchar)', '', ''], ['images', 'row("thumbnail_url" varchar, "medium_url" varchar, "picture_url" varchar, "xl_picture_url" varchar)', '', ''], ['host', 'row("host_id" varchar, "host_url" varchar, "host_name" varchar, "host_location" varchar, "host_about" varchar, "host_response_time" varchar, "host_thumbnail_url" varchar, "host_picture_url" varchar, "host_neighbourhood" varchar, "host_response_rate" bigint, "host_is_superhost" boolean,...', '', ''], ['address', 'row("street" varchar, "suburb" varchar, "government_area" varchar, "market" varchar, "country" varchar, "country_code" varchar, "location" row("type" varchar, "coordinates" array(double), "is_location_exact" boolean))', '', ''], ['availability', 'row("availability_30" bigint, "availability_60" bigint, "availability_90" bigint, "availability_365" bigint)', '', ''], ['review_scores', 'row("review_scores_accuracy" bigint, "review_scores_cleanliness" bigint, "review_scores_checkin" bigint, "review_scores_communication" bigint, "review_scores_location" bigint, "review_scores_value" bigint, "review_scores_rating" bigint)', '', ''], ['reviews', 'array(row("_id" varchar, "date" timestamp, "listing_id" varchar, "reviewer_id" varchar, "reviewer_name" varchar, "comments" varchar))', '', '']], 'sample_row_data': [['1001265', 'https://www.airbnb.com/rooms/1001265', 'Ocean View Waikiki Marina w/prkg', "A short distance from Honolulu's billion dollar mall, and the same distance to Waikiki. Parking included. A great location that work perfectly for business, education, or simple visit. Experience Yacht Harbor views and 5 Star Hilton Hawaiian Village.", 'Great studio located on Ala Moana across the street from Yacht Harbor and near Ala Moana Shopping Center. Studio kitchette, parking, wifi, TV, A/C. Amenities include pool, hot tub and tennis. Sweet ocean views with nice ocean breezes.', "A short distance from Honolulu's billion dollar mall, and the same distance to Waikiki. Parking included. A great location that work perfectly for business, education, or simple visit. Experience Yacht Harbor views and 5 Star Hilton Hawaiian Village. Great studio located on Ala Moana across the...", 'You can breath ocean as well as aloha.', '', 'Honolulu does have a very good air conditioned bus system.', 'Pool, hot tub and tennis', 'We try our best at creating, simple responsive management which never bothers the guest.', 'The general welfare and well being of all the community.', 'Condominium', 'Entire home/apt', 'Real Bed', '3', '365', 'strict_14_with_grace_period', '2019-03-05 21:00:00.000', '2019-03-05 21:00:00.000', '2013-05-23 21:00:00.000', '2019-02-06 21:00:00.000', 2, 1, 1, 96, '[ "TV", "Cable TV", "Wifi", "Air conditioning", "Pool", "Kitchen", "Free parking on premises", "Elevator", "Hot tub", "Washer", "Dryer", "Essentials", "Shampoo", "Hangers", "Hair dryer", "Iron", "Laptop friendly workspace", "Self check-in", "Lockbox", "Hot water", "Bed linens", "Extra pillows...', '[ "", "", "https://a0.muscache.com/im/pictures/15037101/5aff14a7_original.jpg?aki_policy=large", "" ]', '[ "5448114", "https://www.airbnb.com/users/show/5448114", "David", "Honolulu, Hawaii, United States", "I have 30 years of experience in the Waikiki Real Estate Market. We specialize in local sales and property management. Our goal is service and aloha. We want to help people enjoy Hawaii.",...', '[ "Honolulu, HI, United States", "Oʻahu", "Primary Urban Center", "Oahu", "United States", "US", "[ \\"Point\\", \\"[ -157.83919, 21.28634 ]\\", true ]" ]', '[ 16, 46, 76, 343 ]', '[ 9, 8, 9, 9, 10, 9, 84 ]', '[ "[ \\"4765259\\", \\"2013-05-23 21:00:00.000\\", \\"1001265\\", \\"6435238\\", \\"Jacqui\\", \\"Our stay was excellent.  The place had a breath taking view.  David was very accommodating with our hotel stay, parking availability and all of our concerns & questions.  He did above and beyond what anyone...']]), ('table_name': 'mongodb.bank.accounts', 'table_columns': [['account_id', 'bigint', '', ''], ['limit', 'bigint', '', ''], ['products', 'array(varchar)', '', '']], 'sample_row_data': [[557378, 10000, '[ "InvestmentStock", "Commodity", "Brokerage", "CurrencyService" ]']]), ('table_name': 'mongodb.bank.customers', 'table_columns': [['username', 'varchar', '', ''], ['name', 'varchar', '', ''], ['address', 'varchar', '', ''], ['birthdate', 'timestamp', '', ''], ['email', 'varchar', '', ''], ['accounts', 'array(bigint)', '', ''], ['tier_and_details', 'row("a15baf69a759423297f11ce6c7b0bc9a" row("tier" varchar, "benefits" array(varchar), "active" boolean, "id" varchar))', '', '']], 'sample_row_data': [['serranobrian', 'Leslie Martinez', 'Unit 2676 Box 9352\nDPO AA 38560', '1974-11-26 06:30:20.000', 'tcrawford@gmail.com', '[ 170945, 951849 ]', '[ "[ \\"Platinum\\", \\"[ \\\\\\"airline lounge access\\\\\\" ]\\", true, \\"a15baf69a759423297f11ce6c7b0bc9a\\" ]" ]']]), ('table_name': 'mongodb.bank.transactions', 'table_columns': [['account_id', 'bigint', '', ''], ['transaction_count', 'bigint', '', ''], ['bucket_start_date', 'timestamp', '', ''], ['bucket_end_date', 'timestamp', '', ''], ['transactions', 'array(row("date" timestamp, "amount" bigint, "transaction_code" varchar, "symbol" varchar, "price" varchar, "total" varchar))', '', '']], 'sample_row_data': [[443178, 66, '1969-02-03 16:00:00.000', '2017-01-02 16:00:00.000', '[ "[ \\"2003-09-08 17:00:00.000\\", 7514, \\"buy\\", \\"adbe\\", \\"19.1072802650074180519368383102118968963623046875\\", \\"143572.1039112657392422534031\\" ]", "[ \\"2016-06-13 17:00:00.000\\", 9240, \\"buy\\", \\"team\\", \\"24.1525632387771480580340721644461154937744140625\\",...']]), ('table_name': 'mongodb.config.system.sessions', 'table_columns': [], 'sample_row_data': []), ('table_name': 'mongodb.local.startup_log', 'table_columns': [['_id', 'varchar', '', ''], ['hostname', 'varchar', '', ''], ['starttime', 'timestamp', '', ''], ['starttimelocal', 'varchar', '', ''], ['cmdline', 'row("net" row("bindIp" varchar))', '', ''], ['pid', 'bigint', '', '']], 'sample_row_data': [['895e93524e30-1709538444729', '895e93524e30', '2024-03-03 23:47:24.000', 'Mon Mar  4 07:47:24.729', '[ "[ \\"*\\" ]" ]', 7]]), ('table_name': 'mongodb.restaurant.sales', 'table_columns': [['saledate', 'timestamp', '', ''], ['storelocation', 'varchar', '', ''], ['customer', 'row("gender" varchar, "age" bigint, "email" varchar, "satisfaction" bigint)', '', ''], ['couponused', 'boolean', '', ''], ['purchasemethod', 'varchar', '', '']], 'sample_row_data': [['2015-08-25 03:01:02.918', 'Seattle', '[ "M", 50, "keecade@hem.uy", 5 ]', False, 'Phone']]), ('table_name': 'mongodb.restaurant.users', 'table_columns': [['name', 'varchar', '', ''], ['email', 'varchar', '', ''], ['password', 'varchar', '', '']], 'sample_row_data': [['Ned Stark', 'sean_bean@gameofthron.es', '$2b$12$UREFwsRUoyF0CRqGNK0LzO0HM/jLhgUCNNIJ9RJAqMUQ74crlJ1Vu']]), ('table_name': 'postgresql.public.document', 'table_columns': [['id', 'integer', '', ''], ['name', 'varchar', '', ''], ['description', 'varchar', '', ''], ['doc_summary', 'varchar', '', ''], ['owner_id', 'integer', '', ''], ['is_active', 'boolean', '', ''], ['chat_history', 'varchar', '', ''], ['texts_4k_token', 'varchar', '', ''], ['texts', 'varchar', '', ''], ['tables', 'varchar', '', ''], ['table_summary', 'varchar', '', '']], 'sample_row_data': [[147, '20240308_Bundle045401_Intapp_ALGoodbodyLLP_v1.pdf', '(/Users/prem/Prem/projects/gds/ai-saas/data/in/,20240308_Bundle045401_Intapp_ALGoodbodyLLP_v1.pdf," document text and table summaries.")', '"[\\"```json\\\\n(\\\\n  \\\\\\"OWNER\\\\\\": \\\\\\"A & L Goodbody LLP\\\\\\",\\\\n  \\\\\\"CUSTOMER\\\\\\": \\\\\\"A & L Goodbody LLP\\\\\\",\\\\n  \\\\\\"BILLING\\\\\\": (\\\\n    \\\\\\"ADDRESS\\\\\\": \\\\\\"International Financial Services Centre, \\\\\\\\nNorth Wall Quay\\\\\\\\nDublin, Ireland D01 H104\\\\\\\\nIreland\\\\\\",\\\\n   ...', None, False, None, '("[\' \\\\n Order and  Sale Agreement #045401 A & L Goodbody  LLP IntappInstructions:\\\\n \\\\n1.Please complete the Contact Information Sheet\\\\n2.Please sign, date and return the Order and Sale Agreement  or Amendment , as applicable, to your contact\\\\n \\\\nContact Information\\\\nSoftware...', '(" \n Order and  Sale Agreement #045401 A & L Goodbody  LLP IntappInstructions:\n \n1.Please complete the Contact Information Sheet\n2.Please sign, date and return the Order and Sale Agreement  or Amendment , as applicable, to your contact\n \nContact Information\nSoftware Delivery\nThe person listed as...', '()', None]]), ('table_name': 'postgresql.public.dummy_model', 'table_columns': [['id', 'integer', '', ''], ['name', 'varchar(200)', '', '']], 'sample_row_data': []), ('table_name': 'postgresql.public.items', 'table_columns': [['id', 'integer', '', ''], ['title', 'varchar', '', ''], ['description', 'varchar', '', ''], ['owner_id', 'integer', '', ''], ['is_active', 'boolean', '', '']], 'sample_row_data': []), ('table_name': 'postgresql.public.orders', 'table_columns': [['orderkey', 'bigint', '', ''], ['orderstatus', 'varchar', '', ''], ['totalprice', 'double', '', ''], ['orderdate', 'varchar', '', '']], 'sample_row_data': [[1, 'San Francisco', 13.0, '']]), ('table_name': 'postgresql.public.users', 'table_columns': [['id', 'integer', '', ''], ['email', 'varchar(50)', '', ''], ['password', 'varchar(50)', '', ''], ['is_active', 'varchar(50)', '', ''], ['is_superuser', 'varchar(50)', '', ''], ['is_verified', 'varchar(50)', '', '']], 'sample_row_data': []), ('table_name': 'postgresql.public.worksheet', 'table_columns': [['id', 'integer', '', ''], ['title', 'varchar', '', ''], ['description', 'varchar', '', ''], ['owner_id', 'integer', '', ''], ['is_active', 'boolean', '', '']], 'sample_row_data': [])]"""

    def revise_question(self, question, history):

        # print ('##### history: ', history)
        # print ('##### question: ', question)

        # Butify the user before shending to sql engine prompt
        prompt_text = """
        System:\n 
        As a helpful assistant, you need to analyze the user question, and the chat context provided below, 
        and carefully rephrase the user's question into a form that can be understood by the SQL agent. Be mindful of identifying 
        reference from the chat history and formulate the question for SQL agent to process the revised question efficiently. 
        Your goal is to ensure the SQL agent can process the revised question efficiently, providing precise answers drawn from 
        the underlying database. Say, user question was 'Get all the details about the users on uploaded file. ', you retrive all user 
        details like first name, last name, email, phone number, address, and other details provided history and write the revised 
        question in plain english. 
        
        """

        # prompt_text += "Database Schema: \n[ " + self.db_schema_str () + "]\n"

        prompt_text += """
  
        Text Context:\n {context}\n

        History:\n {history}?\n

        Question:\n {question}?\n

        Answer: """

        context = [self.get_document_obj(
            "The user question is related to the file they uploaded or previous conversion which is provided in chat history. ")]

        response = self.user_input_nofaiss(prompt_text=prompt_text, user_question=question, history=history,
                                           docs=context)

        print("#######revised Question:####### ", response["output_text"])
        print()

        return response["output_text"]

    def process_file_and_summarize(self, fname, full_response=None):
        # Extract the PDF content and return it in JSON format
        pdf_content = self.extract_pdf_content(fname)
        # print(pdf_content)

        # Convert the content dictionary to a JSON string
        # json_obj = json.loads(pdf_content)

        # Print the JSON string
        print('PDF text: ', (pdf_content))

        text_chunks = self.get_text_chunks(pdf_content)
        self.get_vector_store(text_chunks)

        prompt_template = """
            As a Contract Management Analyst, please answer the following questions in a key-value pair JSON format. 
            Each key corresponds to the question key, and the value is your response. Avoid repeating the question; provide only 
            the response. If you don't know the anwser to the question, mark "na" in the response. 

            The questions are:
                OWNER - Who is the owner of the contract?
                CUSTOMER - With whom has the contract been signed?
                BILLING - List the billing address and contact details on the contract. Clarify if there are specific billing contacts or multiple addresses involved.
                KEY_SECTION - List all key sections on the provided contract document. Specify if you are looking for specific types of sections, such as legal, financial, or operational.
                CONTACT_DETAILS - List all contact details with their respective contract names, emails, and others. Specify the types of contacts, like parties involved or points of contact.
                GRAND_TOTAL - What is the grand total for the entire contract duration? Specify the currency for clarity.
                SUB_LIST - What is the total amount per year for these subscriptions? List all. Ask for a breakdown of the subscriptions and their associated yearly amounts.
                SERVICE_LIST - List all services covered under this contract. Specify if there are specific categories of services or types of deliverables.
                START_DATE - What is the start date of the contract?
                END_DATE - What is the end date of the contract?
                INSIGHTS - Can you provide insights about the contract? For example, unique clauses or conditions. Encourage a more detailed analysis by asking for specific examples of unique clauses or conditions.
                PENALTIES - Are there any penalties or conditions for early termination of the contract?
                RENEWAL_CLOUS - Are there any renewal options in the contract? if yes, list the renewal terms and conditions.
                PAYMENT_TERMS - What are the payment terms outlined in the contract?
                OBLIGATIONS - Are there specific obligations or responsibilities for each party in the contract?
                CONF_DISCLOSURE - List the confidentiality or non-disclosure agreements listed on the contract.
                INV_REQ - list the Invoicing Requirements in the contract.
                INV_CONTACT - list the Invoicing contact in the contract.
                SOFT_CONTACT - list the software delivery contact in the contract.
                ADD_QUESTION - Awnser Additional Question: \n{question}\n
                
            Text Context:\n {context}?\n

            Answer:
            """
        question = "hello  "

        response = self.user_input(question, prompt_template)

        for item in response['output_text']:
            full_response += item

        return text_chunks, full_response
