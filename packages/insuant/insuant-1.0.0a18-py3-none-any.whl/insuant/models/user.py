from insuant.database import Base
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, DateTime, Boolean


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(255), nullable=False)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f'<User {self.username}>'


class UserApiLimit(Base):
    __tablename__ = 'user_api_limit'

    id = Column(String, primary_key=True, default=func.uuid_generate_v4())
    user_id = Column(String, unique=True)
    count = Column(Integer, default=0)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __repr__(self):
        return f'<UserApiLimit {self.user_id}>'


class UserSubscription(Base):
    __tablename__ = 'user_subscription'

    id = Column(String, primary_key=True, default=func.uuid_generate_v4())
    user_id = Column(String, unique=True)
    stripe_customer_id = Column(String, unique=True)
    stripe_subscription_id = Column(String, unique=True)
    stripe_price_id = Column(String)
    stripe_current_period_end = Column(DateTime)

    def __repr__(self):
        return f'<UserSubscription {self.user_id}>'
