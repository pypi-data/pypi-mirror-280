import enum
from datetime import datetime
# from enum import Enum
from typing import Optional, Dict

from sqlalchemy.orm import backref
from sqlmodel import Field, SQLModel, Column, Relationship, Enum, JSON


class ActionTypeEnum(Enum):
    ask_question = 'ask_question'
    upload_file = 'upload_file'
    write_code = 'write_code'
    create_report = 'create_report'


class SystemActionTypeEnum(Enum):
    query_agent = 'query_agent'
    doc_agent = 'doc_agent'
    sql_agent = 'sql_agent'
    report_agent = 'report_agent'
    code_agent = 'code_agent'


class ActionDetails(SQLModel, __tablename__="action_details", table=True):
    id: int = Field(default=None, primary_key=True, unique=True, index=True)
    action_type: str = Field(max_length=255)
    details: Optional[dict] = Field(default=None, sa_column=Column(JSON))


class UserInteraction(SQLModel, table=True, __tablename__="user_interactions"):
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(default=None, foreign_key="users.id")
    session_name: str = Field(max_length=255)
    timestamp: datetime = Field(default=None)

    interaction_task: list["InteractionTask"] = Relationship(back_populates="user_interaction")


class InteractionTask(SQLModel, table=True, __tablename__="interaction_task"):
    id: int = Field(default=None, primary_key=True, unique=True, index=True)
    user_interactions_id: int = Field(default=None, foreign_key="userinteraction.id")

    user_request: list["UserRequest"] = Relationship(back_populates="interaction")
    system_responses: list["SystemResponse"] = Relationship(back_populates="systemResponse")
    user_interaction: list["UserInteraction"] = Relationship(back_populates="interaction_task")


class UserRequest(SQLModel, table=True, __tablename__="user_request"):
    id: int = Field(default=None, primary_key=True, unique=True, index=True)
    interaction_task_id: int = Field(
        default=None, foreign_key="interactiontask.id"
    )
    user_id: int = Field(default=None, foreign_key="users.id")
    action_type: str = Field(max_length=255)
    timestamp: datetime = Field(default=None)
    details: Optional[dict] = Field(default=None, sa_column=Column(JSON))
    interaction: list["InteractionTask"] = Relationship(back_populates="user_request")

class SystemResponse(SQLModel, table=True, __tablename__="system_responses"):
    id: int = Field(default=None, primary_key=True, unique=True, index=True)
    interaction_task_id: int = Field(
        default=None, foreign_key="interactiontask.id"
    )
    response_type: str = Field(max_length=255)
    timestamp: datetime = Field(default=None)
    details: Optional[dict] = Field(default=None, sa_column=Column(JSON))
    systemResponse: list["InteractionTask"] = Relationship(back_populates="system_responses")
