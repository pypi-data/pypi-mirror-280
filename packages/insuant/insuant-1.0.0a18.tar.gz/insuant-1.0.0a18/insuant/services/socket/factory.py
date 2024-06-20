from typing import TYPE_CHECKING

from insuant.services.factory import ServiceFactory
from insuant.services.socket.service import SocketIOService

if TYPE_CHECKING:
    from insuant.services.cache.service import CacheService


class SocketIOFactory(ServiceFactory):
    def __init__(self):
        super().__init__(
            service_class=SocketIOService,
        )

    def create(self, cache_service: "CacheService"):
        return SocketIOService(cache_service)
