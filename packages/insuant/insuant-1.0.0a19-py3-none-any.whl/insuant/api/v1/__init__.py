from insuant.api.v1.api_key import router as api_key_router
from insuant.api.v1.chat import router as chat_router
from insuant.api.v1.endpoints import router as endpoints_router
from insuant.api.v1.files import router as files_router
from insuant.api.v1.flows import router as flows_router
from insuant.api.v1.login import router as login_router
from insuant.api.v1.monitor import router as monitor_router
from insuant.api.v1.store import router as store_router
from insuant.api.v1.users import router as users_router
from insuant.api.v1.validate import router as validate_router
from insuant.api.v1.variable import router as variables_router
from insuant.api.v1.auth import router as insuant_auth_router
from insuant.api.v1.chats import router as insuant_chats_router
from insuant.api.v1.documents import router as insuant_docs_router
from insuant.api.v1.interact import router as insuant_interact_router
from insuant.api.v1.flowPublish import router as flowpublish_router
# from insuant.api.v1.account import router as account_router

__all__ = [
    "chat_router",
    "endpoints_router",
    "store_router",
    "validate_router",
    "flows_router",
    "users_router",
    "api_key_router",
    "login_router",
    "variables_router",
    "monitor_router",
    "files_router",
    "insuant_auth_router",
    "insuant_chats_router",
    "insuant_docs_router",
    "insuant_interact_router",
    "flowpublish_router"
    # "account_router"
]
