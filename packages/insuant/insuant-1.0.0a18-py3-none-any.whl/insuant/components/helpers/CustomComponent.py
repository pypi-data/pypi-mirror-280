# from insuant.field_typing import Data
from insuant.schema import Record
from insuant.interface.custom.custom_component import CustomComponent


class Component(CustomComponent):
    display_name = "Custom Component"
    description = "Use as a template to create your own component."
    documentation: str = "http://docs.insuant.org/components/custom"
    icon = "custom_components"

    def build_config(self):
        return {"param": {"display_name": "Parameter"}}

    def build(self, param: str) -> Record:
        return Record(data=param)
