from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from insuant.database import get_db
from insuant.services.insuant.auth_service import AuthService as auth
from insuant.services.insuant.api_limit_service import get_user_api_limit,increment_user_api_limit

router = APIRouter(prefix="/user-api-limits")

@router.get("/api/get-user-api/{user_id}")
async def get_api_limit_count(
    user_id: str,
    current_user: auth.User = Depends(auth.get_current_active_user),
    session: Session = Depends(get_db)
):
    try:
        user_api_limit = get_user_api_limit(session, user_id)
        if user_api_limit:
            return {"count": user_api_limit.count}
        else:
            return {"count": 0}
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Failed to get user API limit count")
    finally:
        session.close()
@router.get("/api/checkapilimit/{user_id}")
async def check_user_api_limit(
    user_id: str,
    current_user: auth.User = Depends(auth.get_current_active_user),
    session: Session = Depends(get_db)
):
    try:
        userapilimit = get_user_api_limit(session, user_id)
        if userapilimit is None:
            raise HTTPException(status_code=404, detail="User API limit not found")

        remaining_limit = userapilimit.count
        return {"remaining": remaining_limit}

    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Failed to check user API limit")
    finally:
        session.close()

@router.put("/api/incrementapilimit/{user_id}")
async def increment_user_api_limit_route(
    user_id: str,
    current_user: auth.User = Depends(auth.get_current_active_user),
    session: Session = Depends(get_db)
):
    try:
        increment_user_api_limit(session, user_id)
        return {"message": "User API limit incremented successfully"}

    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Failed to increment user API limit")
    finally:
        session.close()