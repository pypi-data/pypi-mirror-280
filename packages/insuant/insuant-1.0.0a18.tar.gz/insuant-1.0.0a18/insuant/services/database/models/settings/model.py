# from datetime import datetime
# from uuid import UUID, uuid4
# from sqlmodel import SQLModel, Field
# class Account(SQLModel, table=True):
#     id: UUID = Field(default_factory=uuid4, primary_key=True, unique=True)
#     user_id:str = Field(index=True, unique=True)
#     name:str = Field(index=True, unique=True)
#     dob:str = Field(default_factory=datetime.utcnow)
#
#     def __repr__(self):
#         return f'<Account {self.user_id}>'