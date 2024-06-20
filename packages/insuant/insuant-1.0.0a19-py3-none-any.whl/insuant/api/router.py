# Router for base api
from fastapi import APIRouter

from insuant.api.v1 import (
    api_key_router,
    chat_router,
    endpoints_router,
    files_router,
    flows_router,
    login_router,
    monitor_router,
    store_router,
    users_router,
    validate_router,
    variables_router,
    insuant_auth_router,
    insuant_chats_router,
    insuant_docs_router,
    insuant_interact_router,
    flowpublish_router
    # account_router
)

router = APIRouter()
router.include_router(insuant_auth_router,prefix="")
router.include_router(insuant_chats_router,prefix="/api/v1/chat")
router.include_router(insuant_docs_router,prefix="/api/v1/doc")
router.include_router(insuant_interact_router,prefix="/api/v1/interact")
router.include_router(chat_router,prefix="/api/v1")
router.include_router(endpoints_router,prefix="/api/v1")
router.include_router(validate_router,prefix="/api/v1")
router.include_router(store_router,prefix="/api/v1")
router.include_router(flows_router,prefix="/api/v1")
router.include_router(users_router,prefix="/api/v1")
router.include_router(api_key_router,prefix="/api/v1")
router.include_router(login_router,prefix="/api/v1")
router.include_router(variables_router,prefix="/api/v1")
router.include_router(files_router,prefix="/api/v1")
router.include_router(monitor_router,prefix="/api/v1")
router.include_router(flowpublish_router, prefix="/api/v1")
# router.include_router(account_router, prefix="/api/v1")
