from datetime import timedelta
from fastapi import status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, HTTPException
from fastapi import Depends
from typing_extensions import Annotated

from insuant.services.insuant.auth_service import AuthService as auth

router = APIRouter(tags=["INSUANT_TOKEN"])


@router.post("/token")
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> auth.Token:
    user = auth.authenticate_user(auth.fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return auth.Token(access_token=access_token, token_type="bearer")

