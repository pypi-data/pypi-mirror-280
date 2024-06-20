from insuant.services.factory import ServiceFactory
from insuant.services.monitor.service import MonitorService
from insuant.services.settings.service import SettingsService


class MonitorServiceFactory(ServiceFactory):
    name = "monitor_service"

    def __init__(self):
        super().__init__(MonitorService)

    def create(self, settings_service: SettingsService):
        return self.service_class(settings_service)
