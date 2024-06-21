from typing import TYPE_CHECKING

from insuant.services.factory import ServiceFactory
from insuant.services.variable.service import VariableService

if TYPE_CHECKING:
    from insuant.services.settings.service import SettingsService


class VariableServiceFactory(ServiceFactory):
    def __init__(self):
        super().__init__(VariableService)

    def create(self, settings_service: "SettingsService"):
        return VariableService(settings_service)
