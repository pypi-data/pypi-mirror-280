from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.query_engine import SubQuestionQueryEngine
from llama_index.core.callbacks import CallbackManager, LlamaDebugHandler
from llama_index.core import Settings
import nest_asyncio
from insuant.interface.custom.custom_component import CustomComponent
from llama_index.core.schema import TextNode
from llama_index.core.text_splitter import SentenceSplitter
import os
from insuant.schema import Record

nest_asyncio.apply()


class DocumentComponent(CustomComponent):
    display_name: str = "Document Agent"
    description: str = "Answer the questions from all the documents"

    def build_config(self):
        # field_type and required are optional
        return {
            "input_value": {"display_name": "Input", "info": "The input to the agent."},
            "document": {
                "display_name": "Document",
            },
            "open_api_key": {
                "display_name": "OPEN API Key",
                "info": "The Open API Key to use for the Google Generative AI.",
            },
        }

    def build(
            self,
            open_api_key: str,
            input_value: str,
            document: Record,
    ) -> str:
        os.environ["OPENAI_API_KEY"] = open_api_key
        # Using the LlamaDebugHandler to print the trace of the sub questions
        # captured by the SUB_QUESTION callback event type
        llama_debug = LlamaDebugHandler(print_trace_on_end=True)
        callback_manager = CallbackManager([llama_debug])

        Settings.callback_manager = callback_manager
        text_splitter = SentenceSplitter(chunk_size=1024)
        
        text_chunks = text_splitter.split_text(str(document))

        nodes = [TextNode(text=chunk) for chunk in text_chunks]
        vector_query_engine = VectorStoreIndex(nodes).as_query_engine()
        query_engine_tools = [
            QueryEngineTool(
                query_engine=vector_query_engine,
                metadata=ToolMetadata(
                    name="qualitative_and_quantitative_query_engine",
                    description="""A query engine that can answer the questions about a set of documents that the user pre-selected for the conversation.
                                        Any questions related to the document should be asked here.""".strip(),
                ),
            ),
        ]

        query_engine = SubQuestionQueryEngine.from_defaults(
            query_engine_tools=query_engine_tools,
            use_async=True,
        )
        response = query_engine.query(str(input_value))
        return str(response)
