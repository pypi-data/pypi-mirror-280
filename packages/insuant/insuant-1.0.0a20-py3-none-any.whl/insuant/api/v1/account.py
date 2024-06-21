# from fastapi import APIRouter, HTTPException, Depends
# from pydantic import BaseModel
# from sqlalchemy.orm import Session
# from insuant.database import get_db
# from insuant.services.insuant.auth_service import AuthService as auth
# from insuant.services.insuant.account_service import create_account, update_account, get_account_by_user_id
#
# router = APIRouter()
#
# class AccountForm(BaseModel):
#     name: str
#     dob: str
#
# @router.post("/api/account")
# async def post_account(account_form: AccountForm, current_user: auth.User = Depends(auth.get_current_active_user),
#                        session: Session = Depends(get_db)):
#     try:
#         created_account = create_account(session, account_form)
#         return created_account
#     except Exception as e:
#         print("Error creating account:", e)
#         raise HTTPException(status_code=500, detail="Failed to create account")
#     finally:
#         session.close()
#
# @router.get("/api/account/{user_id}", response_model=AccountForm)
# async def get_account(user_id: str, current_user: auth.User = Depends(auth.get_current_active_user),
#                       session: Session = Depends(get_db)):
#     try:
#         account = get_account_by_user_id(session, user_id)
#         if not account:
#             raise HTTPException(status_code=404, detail="Account not found")
#         return account
#     except Exception as e:
#         print("Error retrieving account:", e)
#         raise HTTPException(status_code=500, detail="Failed to retrieve account")
#     finally:
#         session.close()
#
# @router.put("/api/account/{user_id}", response_model=AccountForm)
# async def put_account(user_id: str, account_form: AccountForm,
#                       current_user: auth.User = Depends(auth.get_current_active_user),
#                       session: Session = Depends(get_db)):
#     try:
#         updated_account = update_account(session, user_id, account_form)
#         return updated_account
#     except Exception as e:
#         print("Error updating account:", e)
#         raise HTTPException(status_code=500, detail="Failed to update account")
#     finally:
#         session.close()