# from sqlalchemy.orm import Session
# from insuant.services.database.models.settings.model import Account
#
# def create_account(db: Session, account: Account):
#     db_account = Account(**account.dict())
#     db.add(db_account)
#     db.commit()
#     db.refresh(db_account)
#     return db_account
#
# def get_account_by_user_id(db: Session, user_id: str):
#     return db.query(Account).filter(Account.user_id == user_id).first()
#
# def update_account(db: Session, user_id: str, account: Account):
#     db_account = db.query(Account).filter(Account.user_id == user_id).first()
#     db_account.name = account.name
#     db_account.dob = account.dob
#     db.commit()
#     db.refresh(db_account)
#     return db_account
