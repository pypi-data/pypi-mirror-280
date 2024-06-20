from typing import Any

from insuant.interface.custom.custom_component import CustomComponent
from llama_index.core import SQLDatabase
from llama_index.core.query_engine import NLSQLTableQueryEngine
from llama_index.core.indices.struct_store import SQLTableRetrieverQueryEngine
from IPython.display import Markdown, display
from sqlalchemy import create_engine
from llama_index.llms.openai import OpenAI
from llama_index.core import ServiceContext, set_global_service_context
from llama_index.core import PromptTemplate
import ast
import os
import llm
import json

class FileUploadComponent(CustomComponent):
    display_name = "SQL Agent using LLAMA Index"
    description = "This component is an implementation of SQLAgent of LLAMA INDEX, which consists in independent subtasks to run in parallel to achieve a task keeping an initial goal/theme."

    def build_config(self):
        return {
            "database_url": {
                "display_name": "Database URL",
                "advanced": False,
                "required": True,
            },
            "model": {
                "display_name": "Model",
                "advanced": False,
                "required": True,
                "options": [
                    # "claude-3-haiku",
                    # "claude-3-sonnet",
                    # "claude-3-opus",
                    "gpt-4-turbo",
                    "gpt-4-0125-preview",
                    "gpt-3.5-turbo",
                ],

            },
            "API_MODEL_KEY": {
                "password": True,
                "required": True,
            },
            "input": {
                "display_name": "Input",
                "info": "Ask Questions related to Database",
            },
            "temperature": {
                "display_name": "Temperature",
                "info": "Set the Temperature for the model",
            },
        }

    def arrayOfQuestions(self, input: str, model: str,API_MODEL_KEY: str) -> Any:
        questionPrompt = """Return only the array. Split the questions and convert it to array from the user questions.If the user question is single question return single question as array. Questions={question} """
        AIModel = llm.get_model(model)
        AIModel.key = API_MODEL_KEY
        questions = AIModel.prompt(questionPrompt.format(question=input))
        print(questions)
        array = ast.literal_eval(questions.text())
        print(array)
        return array

    def build(self, input: str, model: str, API_MODEL_KEY: str, database_url: str, temperature: float) -> str:
        os.environ["OPENAI_API_KEY"] = API_MODEL_KEY
        openllm = OpenAI(model=model, temperature=temperature)
        openllm.api_key = API_MODEL_KEY
        service_context = ServiceContext.from_defaults(llm=openllm)
        engine = create_engine(database_url, pool_size=20, max_overflow=0, echo=True)

        db = SQLDatabase(engine)
        query_engine = NLSQLTableQueryEngine(db, service_context=service_context)
        questions = self.arrayOfQuestions(input, model, API_MODEL_KEY)
        prompt = """"""
        answers = {}
        for question in questions:
            print(question)
            response = query_engine.query("Please craft your query without employing semicolons, and ensure it solely pertains to the table schema. \n " + question)
            answers[question] = str(response)
            print(response)
        json_string = json.dumps(answers, indent=4)
        json_obj = json.loads(json_string)
        result = ""
        for index, (key, value) in enumerate(json_obj.items(), start=1):
            result += f"{index}. {value} /n"
        return result

