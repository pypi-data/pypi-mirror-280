from insuant.services.factory import ServiceFactory
from insuant.services.settings.service import SettingsService
from insuant.services.state.service import InMemoryStateService


class StateServiceFactory(ServiceFactory):
    def __init__(self):
        super().__init__(InMemoryStateService)

    def create(self, settings_service: SettingsService):
        return InMemoryStateService(
            settings_service,
        )
