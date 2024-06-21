from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from fastapi.security import OAuth2PasswordRequestForm
from insuant.api.v1.schemas import Token
from insuant.services.auth.utils import (
    authenticate_user,
    create_refresh_token,
    create_user_longterm_token,
    create_user_tokens,
)
from insuant.services.deps import (
    get_session,
    get_settings_service,
    get_variable_service,
)
from insuant.services.settings.manager import SettingsService
from insuant.services.variable.service import VariableService
from sqlmodel import Session

router = APIRouter(tags=["Login"])

@router.get("/auto_login")
async def auto_login(
    response: Response,
    db: Session = Depends(get_session),
    settings_service=Depends(get_settings_service),
    variable_service: VariableService = Depends(get_variable_service),
):
    auth_settings = settings_service.auth_settings
    if settings_service.auth_settings.AUTO_LOGIN:
        user_id, tokens = create_user_longterm_token(db)
        response.set_cookie(
            "access_token_lf",
            tokens["access_token"],
            httponly=auth_settings.ACCESS_HTTPONLY,
            samesite=auth_settings.ACCESS_SAME_SITE,
            secure=auth_settings.ACCESS_SECURE,
            expires=None,  # Set to None to make it a session cookie
        )
        variable_service.initialize_user_variables(user_id, db)
        return tokens

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail={
            "message": "Auto login is disabled. Please enable it in the settings",
            "auto_login": False,
        },
    )
