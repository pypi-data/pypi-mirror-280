
from insuant.models.user import UserApiLimit as UserApiLimitModel
from pydantic import BaseModel
from sqlalchemy.orm import Session


class UserApiLimit(BaseModel):
    user_id: str
    count: int
class UserApiLimitUpdate(BaseModel):
    count: int

def get_user_api_limit(session: Session, user_id: str):
    return session.query(UserApiLimitModel).filter_by(user_id=user_id).first()


def increment_user_api_limit(session: Session, user_id: str):
    userapilimit = get_user_api_limit(session, user_id)
    if userapilimit:
        userapilimit.count += 1
        session.commit()
    else:
        new_user_api_limit = UserApiLimitModel(user_id=user_id, count=1)
        session.add(new_user_api_limit)
        session.commit()