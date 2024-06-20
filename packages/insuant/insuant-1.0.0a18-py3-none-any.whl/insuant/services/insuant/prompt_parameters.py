import os

import yaml


class PromptService:

    def __init__(self):
        with open(os.path.join(os.getcwd(), 'config.yaml'), 'r') as f:
            data = yaml.full_load(f)

        self.classify_user_question_prompt = str(data["customer"]["prompts"]["chat_service"]["classify_user_question_prompt"])
        self.extract_from_document_prompt = str(data["customer"]["prompts"]["chat_service"]["extract_from_document_prompt"])
        self.plan_user_question_prompt = str(data["customer"]["prompts"]["chat_service"]["plan_user_question_prompt"])
        self.format_user_response_prompt = str(data["customer"]["prompts"]["chat_service"]["format_user_response_prompt"])
        self.db_schema_str = str(data["customer"]["prompts"]["sql_service"]["db_schema_str"])
        self.examples = data["customer"]["prompts"]["sql_service"]["examples"]
        self.generate_text_summaries_prompt = str(data["customer"]["prompts"]["google_service"]["generate_text_summaries_prompt"])
        self.chat_with_docs_prompt = str(data["customer"]["prompts"]["google_service"]["chat_with_docs_prompt"])
        self.chat_with_single_doc_prompt = str(data["customer"]["prompts"]["google_service"]["chat_with_single_doc_prompt"])
        self.connection_string = str(data["customer"]["connection_string"])

        self.config = {
            "classify_user_question_prompt": self.classify_user_question_prompt,
            "extract_from_document_prompt": self.extract_from_document_prompt,
            "plan_user_question_prompt": self.plan_user_question_prompt,
            "format_user_response_prompt": self.format_user_response_prompt,
            "db_schema_str": self.db_schema_str,
            "examples": self.examples,
            "generate_text_summaries_prompt": self.generate_text_summaries_prompt,
            "chat_with_docs_prompt": self.chat_with_docs_prompt,
            "chat_with_single_doc_prompt": self.chat_with_single_doc_prompt,
            "connection_string": self.connection_string,
        }

    def getConfig(self, value):
        return self.config.get(value)
