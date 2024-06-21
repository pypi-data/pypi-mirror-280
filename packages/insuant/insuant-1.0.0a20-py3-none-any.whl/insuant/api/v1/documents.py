from fastapi import APIRouter
from fastapi import Depends

from fastapi.responses import FileResponse
from insuant.services.insuant.auth_service import AuthService as auth
from pydantic import BaseModel, Json
from typing_extensions import Annotated
from insuant.services.insuant.doc_service import DocService


router = APIRouter(tags=["INSUANT_DOCUMENTS"])


class DocumentRouter(BaseModel):
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


@router.post("/analysis")
async def doc_analysis(
        form_data: DocumentRouter,
        current_user: Annotated[auth.User, Depends(auth.get_current_active_user)],
):
    print("####### Inside DocService Init ###########")
    fname = form_data.message.get('fname')
    fpath = form_data.message.get('fpath')
    print("fname: ", fname, " fpath: ", fpath)
    # fname = "DCStandardExample.pdf"
    # fpath = "/Users/prem/Prem/projects/gds/ai-saas/data/in/"
    ds = DocService()
    ds.analysis_document(fpath, fname)
    # print("exit ds.doc: ", ds.doc.doc_summary)

    return ds.doc


@router.post("/list")
async def doc_list(
        current_user: Annotated[auth.User, Depends(auth.get_current_active_user)],
):
    print("## Inside DocService List ##")
    ds = DocService()
    doclist = ds.retrieve_summary_list()
    # print("exit doc list: ", doc_list)

    return doclist


@router.post("/chat")
async def doc_chat(
        form_data: DocumentRouter,
        current_user: Annotated[auth.User, Depends(auth.get_current_active_user)],
):
    print("## Inside DocService Chat ##")
    ds = DocService()
    chat_history = form_data.message.get('chat_history')
    question = form_data.message.get('question')
    doc_id = form_data.message.get('doc_id')
    response = ds.chat_with_document(doc_id, question, chat_history)
    # print("exit doc chat: ", ds.doc.chat_history)

    return response

@router.post("/file")
async def get_file(
        form_data: DocumentRouter,
        current_user: Annotated[auth.User, Depends(auth.get_current_active_user)],):
    fname = form_data.message.get('fname')
    fpath = form_data.message.get('fpath')
    file_path = fpath+fname
    return FileResponse(path=file_path, filename=fname)

@router.post("/chat-all-docs")
async def doc_chat(
        form_data: DocumentRouter,
        current_user: Annotated[auth.User, Depends(auth.get_current_active_user)],
):
    print("## Inside DocService chat-all-docs")
    ds = DocService()
    chat_history = form_data.message.get('chat_history')
    question = form_data.message.get('question')
    response = ds.chat_with_all_documents(question, chat_history)
    # print("exit doc chat: ", ds.doc.chat_history)

    return response

# "message" : "{\"fname\": \"DCStandardExample.pdf\", \"fpath\": \"/Users/prem/Prem/projects/gds/ai-saas/data/in/\"}"

# Replace special characters in ds.doc
# response = re.sub(r'/\\n|\\\\|\{n|n\}|,n|"n|\}n|\\\"n|json/g', '', str(ds.doc))
# print("ds doc", response)

# document_json = json.dumps(ds.doc)
# document_json = re.sub(r'\\n|\\\\|`/g', '', document_json)
# print("json ", document_json)

# print(document_json.file)  # Output: file.txt
# ds.doc.doc_summery = ds.doc.doc_summery.regexp_replace(r'\\n', '\n').regexp_replace(r'\\n', '\n').regexp_replace(r'\\', '')
# ds.doc.doc_summery = re.sub(r'\n', '<br>', ds.doc.doc_summery)
# ds.doc.doc_summery = re.sub(r'\\n|\\\\|`', '', ds.doc.doc_summery)
