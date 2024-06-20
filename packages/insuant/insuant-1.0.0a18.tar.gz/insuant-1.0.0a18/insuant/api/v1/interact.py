from fastapi import APIRouter
from fastapi import Depends
from insuant.models.interact import UserInteraction
from insuant.services.insuant.auth_service import AuthService as auth
from pydantic import BaseModel, Json
from typing_extensions import Annotated
from insuant.services.insuant.interact_service import InteractService

router = APIRouter(tags=["INSUANT_INTERACT"])


class InteractRouter(BaseModel):
    """
    Represents a document request.

    Args:
        message (Json): The message for the request.
        response (Json): The response for the request.
        ... (optional): Add more fields as needed.
    """
    message: Json
    response: str = None
    # Add more fields as needed


@router.post("/sessions")
async def retrive_all_sessions(
        current_user: Annotated[auth.User, Depends(auth.get_current_active_user)],
):
    iService = InteractService()
    return iService.get_all_sessions()


@router.post("/interact")
async def retrive_interact(
        form_data: InteractRouter,
        current_user: Annotated[auth.User, Depends(auth.get_current_active_user)],
):
    id = form_data.message.get('id')
    print("id: ", id)

    iService = InteractService()
    return iService.get_user_interaction(id)


@router.post("/create")
async def create_interact(
        form_data: InteractRouter,
        current_user: Annotated[auth.User, Depends(auth.get_current_active_user)],
):
    msg = form_data.message

    print("msg: ", msg, " current_user: ", current_user)

    iService = InteractService()
    ui = UserInteraction(user_id=msg.get('user_id'), session_name=msg.get('session_name'),
                         timestamp=msg.get('timestamp'))

    return iService.create_user_interaction(ui)


@router.post("/update")
async def update_interact(
        form_data: InteractRouter,
        current_user: Annotated[auth.User, Depends(auth.get_current_active_user)],
):
    fname = form_data.message.get('fname')
    fpath = form_data.message.get('fpath')
    print("fname: ", fname, " fpath: ", fpath)

    iService = InteractService()
    return iService.update_user_interaction()

# {"message": "{\"UserInteraction\": {\"user_id\": 1, \"timestamp\": \"2022-01-01T00:00:00Z\",}}",
#  "response": "string"
# }
