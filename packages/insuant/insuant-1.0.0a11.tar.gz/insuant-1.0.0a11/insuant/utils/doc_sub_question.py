from llama_index.core.schema import TextNode
from llama_index.core.text_splitter import SentenceSplitter
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings, Document
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.query_engine import SubQuestionQueryEngine
from llama_index.core.callbacks import CallbackManager, LlamaDebugHandler, CBEventType, EventPayload


class DocSubQuestion:
    def __init__(self):
        print("doc_sub_question_utils")

    def doc_chat(self, docs, question):
        llama_debug = LlamaDebugHandler(print_trace_on_end=True)
        callback_manager = CallbackManager([llama_debug])
        Settings.callback_manager = callback_manager

        # text_splitter = SentenceSplitter(chunk_size=1024)
        # text_chunks = text_splitter.split_text(str(docs))
        documents = []
        i = 1
        for doc in docs:
            documents.append(Document(id=i, text=doc["doc"], file_name=doc["file"]))
            i = i+1

        vector_query_engine = VectorStoreIndex.from_documents(
                documents,
                use_async=True,
            ).as_query_engine()

        query_engine_tools = [
            QueryEngineTool(
                query_engine=vector_query_engine,
                metadata=ToolMetadata(
                    name="qualitative_and_quantitative_query_engine",
                    description="""A query engine that can answer the questions about a set of documents that the user pre-selected for the conversation.
                                Any questions related to the document should be asked here. answer from the documents only.""".strip(),
                ),
            ),
        ]

        query_engine = SubQuestionQueryEngine.from_defaults(
            query_engine_tools=query_engine_tools,
            use_async=True,
        )
        response = query_engine.query(str(question))
        # for i, (start_event, end_event) in enumerate(
        #         llama_debug.get_event_pairs(CBEventType.SUB_QUESTION)
        # ):
        #     qa_pair = end_event.payload[EventPayload.SUB_QUESTION]
        #     print("Sub Question " + str(i) + ": " + qa_pair.sub_q.sub_question.strip())
        #     # yield "Sub Question " + str(i) + ": " + qa_pair.sub_q.sub_question.strip()
        #     print("Answer: " + qa_pair.answer.strip())
        #     # yield "Answer: " + qa_pair.answer.strip()
        #     print("====================================")

        return str(response)
