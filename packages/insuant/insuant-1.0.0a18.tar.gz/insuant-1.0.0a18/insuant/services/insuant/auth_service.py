from datetime import datetime, timedelta, timezone
from typing import Union
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from typing_extensions import Annotated


class AuthService:
    # to get a string like this run:
    # openssl rand -hex 32brew link python@3.10
    SECRET_KEY = "ed30fc4af0345dfcc4b1cf0b83f1c8e3ec2d28649136594fd39a14e9fd6820aa"
    ALGORITHM = "HS384"
    ACCESS_TOKEN_EXPIRE_MINUTES = 13

    fake_users_db = {
        "apiuser": {
            "username": "apiuser",
            "full_name": "api user",
            "email": "info@gogds.net",
            "hashed_password": "$2b$12$Q8Owole5U1UN.7c0Umob0.Xt7M.pPCpXFEF2hMxR8/CsOHxUezyqe",
            "disabled": False,
        }
    }

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    class Token(BaseModel):
        access_token: str
        token_type: str

    class TokenData(BaseModel):
        username: Union[str, None] = None

    class User(BaseModel):
        username: str
        email: Union[str, None] = None
        full_name: Union[str, None] = None
        disabled: Union[bool, None] = None

    class UserInDB(User):
        hashed_password: str

    def verify_password( plain_password, hashed_password):
        return AuthService.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash( password):
        return AuthService.pwd_context.hash(password)

    def get_user( db, username: str):
        if username in db:
            user_dict = db[username]
            return AuthService.UserInDB(**user_dict)

    def authenticate_user(fake_db, username: str, password: str):
        user = AuthService.get_user(fake_db, username)
        if not user:
            return False
        if not AuthService.verify_password(password, user.hashed_password):
            return False
        return user

    def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, AuthService.SECRET_KEY, algorithm=AuthService.ALGORITHM)
        return encoded_jwt

    async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, AuthService.SECRET_KEY, algorithms=[AuthService.ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            token_data = AuthService.TokenData(username=username)
        except JWTError:
            raise credentials_exception
        user = AuthService.get_user(AuthService.fake_users_db, username=token_data.username)
        if user is None:
            raise credentials_exception
        return user

    async def get_current_active_user(
            current_user: Annotated[User, Depends(get_current_user)]
    ):
        if current_user.disabled:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user
