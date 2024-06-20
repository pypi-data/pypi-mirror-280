import asyncio
import json

from insuant.services.insuant.prompt_parameters import PromptService
from insuant.services.insuant.sql_service import SQL_Service
from langchain_community.retrievers import TavilySearchAPIRetriever
import llm
import os
from dotenv import load_dotenv
from insuant.utils.doc_sub_question import DocSubQuestion
from llama_index.core.schema import TextNode, Document
from llama_index.core.text_splitter import SentenceSplitter
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.query_engine import SubQuestionQueryEngine
from llama_index.core.callbacks import CallbackManager, LlamaDebugHandler, CBEventType, EventPayload

load_dotenv()


class ChatService:
    def __init__(self):
        print("####### Inside ChatService Init ###########")
        os.environ["LANGCHAIN_TRACING_V2"] = "true"
        os.environ["LANGCHAIN_PROJECT"] = "Chat Assistant"
        os.environ["LANGCHAIN_API_KEY"] = os.getenv('LANGCHAIN_API_KEY')
        self.chats = []
        self.ds = DocSubQuestion()
        self.ps = PromptService()

    def get_all_chats(self):
        return self.chats

    def add_chat(self, chat):
        self.chats.append(chat)
        return chat

    def doc_chat(self, doc, question):
        llama_debug = LlamaDebugHandler(print_trace_on_end=True)
        callback_manager = CallbackManager([llama_debug])
        Settings.callback_manager = callback_manager

        # text_splitter = SentenceSplitter(chunk_size=1024)
        # text_chunks = text_splitter.split_text(str(doc))

        # nodes = [TextNode(text=chunk) for chunk in text_chunks]
        documents = [Document(id=1, text=str(doc))]
        vector_query_engine = VectorStoreIndex.from_documents(
            documents,
            use_async=True,
        ).as_query_engine()
        query_engine_tools = [
            QueryEngineTool(
                query_engine=vector_query_engine,
                metadata=ToolMetadata(
                    name="Document_Query_engine",
                    description="""A query engine that can answer the questions about a set of documents that the user pre-selected for the conversation.
                                Any questions related to the document should be asked here. If the question not related 
                                to the document, reply with context not provided""".strip(),
                ),
            ),
        ]

        query_engine = SubQuestionQueryEngine.from_defaults(
            query_engine_tools=query_engine_tools,
            use_async=True,
        )
        response = query_engine.query(str(question))
        for i, (start_event, end_event) in enumerate(
                llama_debug.get_event_pairs(CBEventType.SUB_QUESTION)
        ):
            qa_pair = end_event.payload[EventPayload.SUB_QUESTION]
            print("Sub Question " + str(i) + ": " + qa_pair.sub_q.sub_question.strip())
            # yield "Generated Document Query #" + str(i+1) + ": \n Question: " + qa_pair.sub_q.sub_question.strip() + "\n"
            print("Answer: " + qa_pair.answer.strip())
            # yield "Answer: " + qa_pair.answer.strip() + "\n \n"
            yield json.dumps({'subquery': 1, 'question': qa_pair.sub_q.sub_question.strip(),
                              'answer': qa_pair.answer.strip()})
            print("====================================")

        return str(response)

    # Chat with all database
    def chat_with_sql_agent(self, question, history):
        api_key = os.getenv('TAVILY_API_KEY')
        tavilyRetriever = TavilySearchAPIRetriever(k=3, api_key=api_key)
        # gService = GoogleService()
        # revisedQuestion = gService.revise_question(question, history)
        AIModel = llm.get_model("gpt-3.5-turbo")
        AIModel.key = os.getenv('OPENAI_API_KEY')

        classify_user_question_prompt = self.ps.getConfig('classify_user_question_prompt')
        classify_user_question_prompt = classify_user_question_prompt.format(question=question)
        ## TODO - Extract "source = upload" file content from history and pass it to below insteald if entier history.
        print("history: ", history)
        # history_data = json.loads(history)
        file_upload_nodes = [item for item in history if item.get('source') == 'upload']
        last_file_upload_node = file_upload_nodes[-1:]
        print("## last_file_upload_node: ", last_file_upload_node)

        # upload_file_content = history_data["value"]
        db_Schema_str = self.ps.getConfig('db_schema_str')

        extract_from_document_prompt = self.ps.getConfig('extract_from_document_prompt')
        extract_from_document_prompt = extract_from_document_prompt.format(question=question,
                                                                           last_file_upload_node=last_file_upload_node)
        # print ("extract_from_document_prompt: ", extract_from_document_prompt)

        response = AIModel.prompt(classify_user_question_prompt)
        print("### classify_user_question_prompt response 1 : ", response)

        json_data = json.loads(response.text())
        if json_data["value"] == 0:
            # yield 'Done \n'
            # yield json.dumps({'subquery': 0, 'question': question,
            #                   'answer': ''})
            data = AIModel.prompt("Your name is insuant.ai. Answer the user question: " + str(json_data["question"]),
                                  stream=True)
            # return {"output": str(data.text())}
            for response in data:
                # print(response)
                yield response

        else:
            # yield "Analyzing... \n \n"
            # response = AIModel.prompt(extract_from_document_prompt)
            response = yield from self.doc_chat(last_file_upload_node, question)
            print("res " + response)
            # print("Extracted from document response : ", response);

            ## Extract last 5 chat history history and pass it to below as context.
            chat_nodes = [item for item in history if item.get('source') == 'chat']
            recent_chat_nodes = chat_nodes[-5:]
            print("## recent_chat_nodes: ", recent_chat_nodes)

            plan_user_question_prompt = self.ps.plan_user_question_prompt
            plan_user_question_prompt = plan_user_question_prompt.format(question=question, response=str(response),
                                                                         db_Schema_str=db_Schema_str)
            plan = AIModel.prompt(plan_user_question_prompt)
            print("#### plan_user_question_list : ", plan)

            sagent = SQL_Service()
            sql_agent = sagent.init_sql_agent()

            response_list = []
            plan_list = []
            i = 0
            for row in json.loads(plan.text()):
                i += 1
                # print("Plan: ", row)
                # Method 1 - LC SQL Agent
                # response_list.append(row)
                if "External" in str(row):
                    results = tavilyRetriever.invoke(question)
                    response = []
                    for result in results:
                        response.append(str(result.page_content))
                    firstTwoNode = response[0:2]
                    # yield "Searching in External : \n"
                    # yield "External Resource: " + str(firstTwoNode) + "\n \n"
                    yield json.dumps({'subquery': 1, 'question': "Searching in External",
                                      'answer': str(firstTwoNode)})
                    # plan_list.append(sql_response)
                    response_list.append(str(firstTwoNode))
                else:
                    # yield "Generated SQL Query #" + str(i) + ": \n"
                    # yield "Question: " + str(row) + "\n"
                    sql_response = sql_agent.invoke({"input": str(row)})
                    # yield "answer: " + str(sql_response["output"]) + "\n \n "
                    # print("### sql_response: ", sql_response)
                    yield json.dumps({'subquery': 1, 'question': str(row),
                                      'answer': str(sql_response["output"])})
                    plan_list.append(sql_response)
                    response_list.append(sql_response["output"])

            format_user_response_prompt = self.ps.getConfig('format_user_response_prompt')
            format_user_response_prompt = format_user_response_prompt.format(question=question,
                                                                             response_list=response_list)
            responses = AIModel.prompt(format_user_response_prompt, stream=True)

            # print("#### plan_user_question_list : ", plan)
            # print("#### plan_answer_list: ", response_list)
            # print('#### Final Response: \n', response)
            # final_response = f"""
            #            "plan":\n {response_list}\n, "response":\n {response}\n
            #    """

            # return {"input": question, "output": str(response), "plan": plan_list}
            yield "Final Response: \n \n "
            # yield json.dumps({'subquery': 0, 'question': question,
            #                   'answer': ''})
            for response in responses:
                # print(response)
                # yield json.dumps({'subquery': 0, 'question': question,
                #                   'answer': str(response)})
                yield response