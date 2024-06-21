from typing import Optional

from langchain_community.utilities.searchapi import SearchApiAPIWrapper
from langchain_community.retrievers import TavilySearchAPIRetriever

from insuant.custom import CustomComponent
from insuant.schema.schema import Record
from insuant.services.database.models.base import orjson_dumps


class TavilySearchApi(CustomComponent):
    display_name: str = "TAVILY SEARCH API"
    description: str = "Real-time search engine results API."
    output_types: list[str] = ["Document"]
    documentation: str = "https://www.searchapi.io/docs/google"
    field_config = {

        "api_key": {
            "display_name": "API Key",
            "field_type": "str",
            "required": True,
            "password": True,
            "info": "The API key to use SearchApi.",
        },
        "input": {
            "display_name": "INPUT",
            "field_type": "str",
            "required": True,
        }
    }

    def build(
        self,
        api_key: str,
        input: str,
    ) -> str:
        retriever = TavilySearchAPIRetriever(k=3, api_key=api_key)
        results = retriever.invoke(input)
        response = []
        output = ""
        for result in results:
            response.append(str(result.page_content))
            output = output + str(result.page_content)
            output += "\n"

        return str(output)
