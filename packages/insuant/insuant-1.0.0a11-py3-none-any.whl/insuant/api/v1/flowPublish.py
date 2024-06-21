from datetime import datetime
from typing import List
from uuid import UUID

import orjson
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from fastapi.encoders import jsonable_encoder
from loguru import logger
from sqlmodel import Session, select

from insuant.api.utils import remove_api_keys, validate_is_component
from insuant.api.v1.schemas import FlowListCreate, FlowListRead
from insuant.initial_setup.setup import STARTER_FOLDER_NAME
from insuant.services.auth.utils import get_current_active_user
from insuant.services.database.models.flow import Flow, FlowCreate, FlowRead, FlowUpdate
from insuant.services.database.models.user.model import User
from insuant.services.deps import get_session, get_settings_service
from insuant.services.settings.service import SettingsService

# build router
router = APIRouter(prefix="/flows/publish", tags=["FlowsPublish"])


@router.post("/", response_model=FlowRead, status_code=201)
def create_flow(
    *,
    session: Session = Depends(get_session),
    flow: FlowCreate,
    current_user: User = Depends(get_current_active_user),
):
    try:
        published_flow = session.exec(
            select(Flow).where(
                (Flow.parent_id == flow.parent_id)   # noqa
            ).where((Flow.type == flow.type))
        ).first()
        if published_flow is None:

            if flow.user_id is None:
                flow.user_id = current_user.id

            db_flow = Flow.model_validate(flow, from_attributes=True)
            db_flow.name = db_flow.name
            db_flow.updated_at = datetime.utcnow()

            session.add(db_flow)
            session.commit()
            session.refresh(db_flow)
            return db_flow
        else:
            published_flow.name = flow.name
            published_flow.description = flow.description
            published_flow.data = flow.data
            published_flow.updated_at = datetime.utcnow()
            session.add(published_flow)
            session.commit()
            session.refresh(published_flow)
            return published_flow

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail=str(e)) from e


# @router.get("/", response_model=list[PublishRead], status_code=200)
# def read_flows(
#     *,
#     current_user: User = Depends(get_current_active_user),
#     session: Session = Depends(get_session),
#     settings_service: "SettingsService" = Depends(get_settings_service),
# ):
#     """Read all flows."""
#     try:
#         auth_settings = settings_service.auth_settings
#         if auth_settings.AUTO_LOGIN:
#             flows = session.exec(
#                 select(Publish).where(
#                     (Publish.user_id == None) | (Publish.user_id == current_user.id)  # noqa
#                 )
#             ).all()
#         else:
#             flows = current_user.flows
#
#         flows = validate_is_component(flows)  # type: ignore
#         flow_ids = [flow.id for flow in flows]
#         # with the session get the flows that DO NOT have a user_id
#         try:
#             example_flows = session.exec(
#                 select(Publish).where(
#                     Publish.user_id == None,  # noqa
#                     Publish.folder == STARTER_FOLDER_NAME,
#                 )
#             ).all()
#             for example_flow in example_flows:
#                 if example_flow.id not in flow_ids:
#                     flows.append(example_flow)  # type: ignore
#         except Exception as e:
#             logger.error(e)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e)) from e
#     return [jsonable_encoder(flow) for flow in flows]
#
