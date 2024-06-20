from fastapi import APIRouter, HTTPException, Depends
from datetime import datetime
from sqlmodel import Session
from insuant.database import SessionLocal,get_db
from insuant.models.user import UserSubscription
from pydantic import BaseModel
from typing_extensions import Annotated
from insuant.services.insuant.auth_service import AuthService as auth


router = APIRouter(prefix="/subscriptions")

class UserSubscriptionCreate(BaseModel):
    user_id: str
    stripe_customer_id: str
    stripe_subscription_id: str
    stripe_price_id: str
    stripe_current_period_end: datetime = None
@router.post("/api/subscriptions")
async def create_subscription(
        current_user: Annotated[auth.User, Depends(auth.get_current_active_user)],
        subscription: UserSubscriptionCreate, session: Session = Depends(get_db)):
    try:
        subscription_obj = UserSubscription()
        subscription_obj.user_id = subscription.user_id
        subscription_obj.stripe_subscription_id = subscription.stripe_subscription_id
        subscription_obj.stripe_customer_id = subscription.stripe_customer_id
        subscription_obj.stripe_price_id = subscription.stripe_price_id
        subscription_obj.stripe_current_period_end = datetime.utcnow()
        session.add(subscription_obj)
        session.commit()
        session.refresh(subscription_obj)
        return {"message": "Subscription created successfully", "data": subscription_obj.dict()}
    except Exception as e:
        print(e)
    finally:
        session.close()


@router.put("/api/subscriptions/{user_id}")
async def update_subscription(
        current_user: Annotated[auth.User, Depends(auth.get_current_active_user)],
        user_id: str, subscription: UserSubscriptionCreate):
    db_session = SessionLocal()
    try:
        subscription_obj = db_session.query(UserSubscription).filter_by(user_id=user_id).first()
        if subscription_obj is None:
            raise HTTPException(status_code=404, detail="Subscription not found")

        subscription_obj.stripe_customer_id = subscription.stripe_customer_id
        subscription_obj.stripe_subscription_id = subscription.stripe_subscription_id
        subscription_obj.stripe_price_id = subscription.stripe_price_id
        subscription_obj.stripe_current_period_end = subscription.stripe_current_period_end

        db_session.commit()

        subscription_data = {
            "user_id": subscription_obj.user_id,
            "stripe_customer_id": subscription_obj.stripe_customer_id,
            "stripe_subscription_id": subscription_obj.stripe_subscription_id,
            "stripe_price_id": subscription_obj.stripe_price_id,
            "stripe_current_period_end": subscription_obj.stripe_current_period_end,
        }

        return {"message": "Subscription updated successfully", "data": subscription_data}
        print("saved")

    except Exception as e:
        print("error",e)
        print("not accepted")
    finally:
        db_session.close()

