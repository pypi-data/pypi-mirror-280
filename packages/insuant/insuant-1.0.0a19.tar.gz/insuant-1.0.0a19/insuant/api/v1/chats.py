from fastapi import APIRouter
from pydantic import Json
from fastapi import Depends
from typing_extensions import Annotated
from insuant.services.insuant.chat_service import ChatService
from insuant.services.insuant.auth_service import AuthService as auth
from fastapi.responses import StreamingResponse

# from fastapi import FormData

# Create a router
router = APIRouter(tags=["INSUANT_CHATS"])

from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: Json
    response: str = None
    # Add more fields as needed


@router.post("/analyze/json")
async def process_chat(
        chat_data: ChatRequest,
        current_user: Annotated[auth.User, Depends(auth.get_current_active_user)],
):
    # Access the data
    data = chat_data.model_dump()  # alternate for dict is model_dump
    # Process the chat data
    return [{"item_id": "Foo", "owner": current_user.username, "data": data}]


# Chat with all database
@router.post("/database/all")
async def process_chat(
        chat_data: ChatRequest,
        current_user: Annotated[auth.User, Depends(auth.get_current_active_user)],
):
    chat_service = ChatService()
    chat_history = chat_data.message.get('chat_history')
    question = chat_data.message.get('question')
    # Access the data
    data = chat_service.chat_with_sql_agent(question, chat_history)
    # Process the chat data
    # return [{"item_id": "Foo", "owner": current_user.username, "data": data}]
    # return data.get('output')
    print("data", data)
    return StreamingResponse(data, media_type="text/event-stream")
