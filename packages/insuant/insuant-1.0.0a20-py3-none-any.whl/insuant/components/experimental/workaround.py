# from insuant import CustomComponent
from insuant.field_typing import Data
from insuant.interface.custom.custom_component import CustomComponent
import subprocess
import sys
import base64
from tempfile import NamedTemporaryFile


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    return 1


install("llm")


class FileUploadComponent(CustomComponent):
    display_name = "Workers Paralel Prompt Chain"
    description = "This component is an implementation of Workers Prompt Chaining (Compatible with different LLM models), which consists in independent subtasks to run in parallel to achieve a task keeping an initial goal/theme."

    def build_config(self):
        return {
            "theme": {
                "display_name": "Theme",
                "advanced": False,
                "required": True,
            },
            "model": {
                "display_name": "Model",
                "advanced": False,
                "required": True,
                "options": [
                    "claude-3-haiku",
                    "claude-3-sonnet",
                    "claude-3-opus",
                    "gpt-4-turbo",
                    "gpt-4-0125-preview",
                    "gpt-3.5-turbo",
                ],

            },
            "web": {
                "display_name": "Additional Information (Web, Book, etc.)",
                "advanced": False,
                "required": False,
                "default": ""

            },
            "detail_text": {
                "display_name": "Detail Text",
                "advanced": False,
                "required": True,
                "default": "No",
                "options": [
                    "Yes",
                    "No"
                ],
            },
            "internal_prompt_theme": {
                "display_name": "Internal Prompt Theme",
                "required": False,
                "default": "Generate a clickworthy title about this topic"
            },
            "internal_prompt_instruction": {
                "display_name": "Internal Prompt Instruction",
                "required": False,
                "default": "Generate a compelling 3 section outline given this information"
            },
            "API_MODEL_KEY": {
                "password": True,
                "required": True,
            }
        }

    def build(self, theme: str, model: str, API_MODEL_KEY: str, detail_text: bool, internal_prompt_theme: str = '',
              internal_prompt_instruction: str = '', web: str = '') -> str:
        """
            Workers Paralel Chain: Start with a small topic and then expand it using paralel workers:
            [User provide a topic -> chain 1 make a title -> chain 1,2,3,n work in paralel to process the subtasks -> return in json]
        """

        def install(package):
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            return 1

        install("llm")
        import llm
        from time import sleep

        # It is that way to allow you changing it to use more models if you need it ;)
        model1 = llm.get_model(model)
        model2 = llm.get_model(model)
        model3 = llm.get_model(model)

        model1.key = API_MODEL_KEY
        model2.key = API_MODEL_KEY
        model3.key = API_MODEL_KEY

        prompt_plan = f'{internal_prompt_theme} {theme}, be creative in this process.'

        if (len(web) > 10):
            prompt_plan += "Here is some additional information to create the topics."

        if (detail_text):
            prompt_plan += "Detail the text as the maximum as you can (I want a lot of topics)"

        code_planner_prompt_response = model1.prompt(
            prompt_plan + '''\n
        {Respond in json format {"newsletter": ["topic1", "topic2", "topic 3", "topic 4", "topic 5", ...]}.''' + str(
                internal_prompt_instruction)
        )

        code_planner_result = code_planner_prompt_response.text()

        function_stubs = json.loads(code_planner_result)["newsletter"]

        function_stub_raw_results = "# " + f"**{theme}**" + "\n\n"

        for stub in function_stubs:
            function_stub_raw_results += "\n" + f"## **{stub}**" + "\n\n"

            if (detail_text):
                code_executor_prompt_response = model1.prompt(
                    f"You are writing a newsletter, write the content in plain text about the: {stub}. Remember the context {prompt_plan}. Remember to return the data as plain text in the maximumparagraphs you can generate I want a really big output."
                )
            else:
                code_executor_prompt_response = model1.prompt(
                    f"You are writing a newsletter, write the content in plain text about the: {stub}. Remember the context {prompt_plan}. Remember to return the data as plain text in 2 or more paragraphs."
                )

            function_stub_raw_results += code_executor_prompt_response.text()

        return function_stub_raw_results
