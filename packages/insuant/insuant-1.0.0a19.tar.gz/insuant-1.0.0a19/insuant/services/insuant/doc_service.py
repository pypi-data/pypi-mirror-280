import os
import shutil
from langchain.text_splitter import CharacterTextSplitter
from unstructured.partition.pdf import partition_pdf
from insuant.services.database.models.document import Document
from insuant.database import SessionLocal
from insuant.services.insuant.google_service import GoogleService
from insuant.utils.file_parser import File_Parser
import PyPDF2
import logging
import json
from insuant.utils.doc_sub_question import DocSubQuestion


class DocService:
    def __init__(self):
        print("####### Inside DocService Init ###########")
        self.db = SessionLocal()
        self.ds = DocSubQuestion()
        # self.texts_4k_token = []
        # self.texts = []
        # self.tables = []
        self.doc = None  # Initialize doc attribute

    # Extract elements from PDF
    def extract_pdf_elements(self, path, fname):
        """
        Extract images, tables, and chunk text from a PDF file.
        path: File path, which is used to dump images (.jpg)
        fname: File name
        """
        return partition_pdf(
            filename=path + fname,
            extract_images_in_pdf=False,
            infer_table_structure=False,
            chunking_strategy="by_title",
            max_characters=4000,
            new_after_n_chars=3800,
            combine_text_under_n_chars=2000,
            image_output_dir_path=path,
        )

    # Categorize elements by type
    def categorize_elements(self, raw_pdf_elements):
        """
        Categorize extracted elements from a PDF into tables and texts.
        raw_pdf_elements: List of unstructured.documents.elements
        """
        tables = []
        texts = []
        for element in raw_pdf_elements:
            if "unstructured.documents.elements.Table" in str(type(element)):
                tables.append(str(element))
            elif "unstructured.documents.elements.CompositeElement" in str(type(element)):
                texts.append(str(element))
        return texts, tables

    # Open the PDF file
    def extract_pypdf_content(self, fname):
        # Open the PDF file
        pdf_file = PyPDF2.PdfReader(fname)

        # Extract the content from each page
        content = []
        for page in pdf_file.pages:
            content.append(page.extract_text())

        # Convert the content to JSON format
        # json_content = json.dumps(content)

        return content

    # Split text into chunks
    def read_and_split_file(self, fpath, fname):
        """
        Analyze a file and return a list of chunks.
        text: String
        """

        # File path
        # fpath = "/Users/prem/Prem/projects/gds/lancho-api/data/"
        # fname = "DC Bundle Example.pdf"
        self.doc.name = fname
        full_path = f"{fpath}{fname}"

        # Get elements
        # raw_pdf_elements = self.extract_pdf_elements(fpath, fname)
        # raw_pdf_elements = self.extract_pypdf_content(full_path)
        # print("raw_pdf_elements: ", raw_pdf_elements)
        # raw_pdf_elements = File_Parser().processFile(file=full_path, parcer="llama")
        print("#### full_path: ", full_path)
        raw_pdf_elements = File_Parser().processFile(file=full_path, )
        print("raw_pdf_elements: ", raw_pdf_elements)

        # Get text, tables
        self.doc.texts, self.doc.tables = self.categorize_elements(raw_pdf_elements)
        self.doc.texts = raw_pdf_elements

        # Optional: Enforce a specific token size for texts
        text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
            chunk_size=4000, chunk_overlap=0
        )
        joined_texts = str(self.doc.texts)
        self.doc.texts_4k_token = text_splitter.split_text(joined_texts)

        self.doc.description = (fpath, fname, " document text and table summaries.")

        # return etexts_4k_token, etexts, etables

    def create_document(self):
        # Create a new document
        self.doc.create(
            self.db,
            name=self.doc.name,
            description=self.doc.description,
            doc_summary=json.dumps(self.doc.doc_summary),
            texts_4k_token=self.doc.texts_4k_token,
            texts=self.doc.texts,
            tables=self.doc.tables,
            owner_id=self.doc.owner_id,
            is_active=self.doc.is_active,
            chat_history=self.doc.chat_history,
        )

    def update_document(self):
        # Create a new document
        self.doc.update(
            self.db,
            id=self.doc.id,
            name=self.doc.name,
            description=self.doc.description,
            doc_summary=json.dumps(self.doc.doc_summary),
            texts_4k_token=self.doc.texts_4k_token,
            texts=self.doc.texts,
            tables=self.doc.tables,
            owner_id=self.doc.owner_id,
            is_active=self.doc.is_active,
            chat_history=self.doc.chat_history,
        )

    def analysis_document(self, fpath, fname):

        # Check if document exists in database
        doc = Document.get_by_name(self.db, fname)
        existing = False

        logging.info(" Retrive Document### ", doc)

        # If document exists, return the records from db
        if doc:
            logging.info("Existig Document.")
            self.doc = doc[0]
            existing = True
            print("existing")
        else:
            logging.info("New document, Parse and update db.")
            # Create a new document
            self.doc = Document()

        # Source file
        source_file = f"{fpath}{fname}"
        # self.doc.name = source_file
        # self.doc.description= (source_file, " document summary")

        # logging.info("Invoking GoogleService.process_file_and_summarize")
        # self.doc.texts_4k_token, self.doc.doc_summary = GoogleService.process_file_and_summarize(source_file)

        # Read and split file irrespective of document exists or not to get the latest summary
        if existing:
            if os.path.isfile(source_file):
                self.read_and_split_file(fpath, fname)
            else:
                path = fpath.replace("/in/", "/out/")
                self.read_and_split_file(path, fname)
        else:
            self.read_and_split_file(fpath, fname)

        logging.info("Invoking GoogleService.generate_text_summaries")
        gs = GoogleService()
        # Get text, table summaries
        self.doc.doc_summary, self.doc.table_summary = gs.generate_text_summaries(
            self.doc.texts_4k_token, self.doc.tables, summarize_texts=True
        )

        if existing and not os.path.isfile(source_file):
            self.update_document()
            doc = Document.get_by_name(self.db, fname)
            self.doc = doc[0]
        elif existing:
            self.update_document()
            doc = Document.get_by_name(self.db, fname)
            self.doc = doc[0]
            destination_folder = fpath.replace("/in/", "/out/")

            print("## source_file: ", source_file, " destination_folder: ", destination_folder)

            # If the destination file exists, remove it
            if os.path.exists(destination_folder + fname):
                print("Removing destination file: ", destination_folder + fname)
                os.remove(destination_folder + fname)

            # Move the file to the destination folder
            shutil.move(source_file, destination_folder)
        else:
            # Create a new document
            self.create_document()

            # Moved out of else block to fix upload issue
            doc = Document.get_by_name(self.db, fname)
            self.doc = doc[0]

            # Specify the destination folder path
            destination_folder = fpath.replace("/in/", "/out/")

            print("## source_file: ", source_file, " destination_folder: ", destination_folder)

            # If the destination file exists, remove it
            if os.path.exists(destination_folder + fname):
                print("Removing destination file: ", destination_folder + fname)
                os.remove(destination_folder + fname)

            # Move the file to the destination folder
            shutil.move(source_file, destination_folder)

    def retrieve_summary_list(self):
        # Retrieve all documents
        return Document.get_summary_list(self.db)
        # return Document.get_summary_list(self.db)

    def chat_with_document(self, doc_id, question, history):
        # Retrieve a document by id
        doc = Document.get_by_name(self.db, doc_id)
        self.doc = doc[0]
        self.doc.chat_history = history
        docs = [{"id": 1, "doc": str(self.doc.texts_4k_token), "file": str(self.doc.name)}]
        # gs = GoogleService()
        # context = [gs.get_document_obj(docs)]
        # print('context ', context)
        # response = gs.chat_with_single_doc(question=question, context=context, history=history)
        response = self.ds.doc_chat(docs, question)

        return str(response)



    def chat_with_all_documents(self, question, history):
        # Retrieve a document by id
        docs = Document.get_all(self.db)

        # gs = GoogleService()

        docs_text = []
        i = 1
        for d in docs:
            # docs_text.append(gs.get_document_obj(d.doc_summary))
            # docs_text.append(gs.get_document_obj('text=[' + d.texts_4k_token + '], summary=[' + d.doc_summary + ']'))
            # docs_text.append(gs.get_document_obj(d.texts_4k_token))
            docs_text.append({"id": i, "doc": d.texts_4k_token, "file": str(d.name)})
            i = i + 1

        print("\n\n all docs: ", str(docs_text))
        # response = gs.chat_with_docs(question=question, context=docs_text, history=history)
        response = self.ds.doc_chat(docs_text, question)
        return response
