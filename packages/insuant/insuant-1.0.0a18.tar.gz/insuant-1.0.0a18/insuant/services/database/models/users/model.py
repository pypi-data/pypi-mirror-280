from sqlmodel import Field, SQLModel, String, Integer, Boolean
from sqlalchemy.sql import func
from datetime import datetime


class Users(SQLModel, table=True, __tablename__="users"):
    id: int = Field(default=None, primary_key=True)
    user_id: str = Field(max_length=255, nullable=False)
    username: str = Field(index=True)
    email: str = Field(unique=True, index=True)
    hashed_password: str = Field(nullable=True)  # Optional password field
    is_active: bool = Field(default=True)


class UserApiLimit(SQLModel, table=True, table_name="user_api_limit"):
    id: str = Field(default=func.uuidgenv4(), primary_key=True)  # Uses SQLModel's uuidgenv4 function
    user_id: str = Field(unique=True)
    count: int = Field(default=0)
    created_at: datetime = Field(default=datetime.now())  # Uses datetime.now() directly
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class UserSubscription(SQLModel, table=True, table_name="user_subscription"):
    id: str = Field(default=func.uuidgenv4(), primary_key=True)  # Uses SQLModel's uuidgenv4 function
    user_id: str = Field(unique=True)
    stripe_customer_id: str = Field(unique=True)
    stripe_subscription_id: str = Field(unique=True)
    stripe_price_id: str = Field(nullable=True)  # Optional price ID
    stripe_current_period_end: datetime = Field(nullable=True)  # Optional end date
