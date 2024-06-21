from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from insuant.database import Base


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


class ActionDetails(Base):
    __tablename__ = 'action_details'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    action_type = Column(String(255))
    details = Column(JSONB)


class UserRequest(Base):
    __tablename__ = 'user_request'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    interaction_task_id = Column(Integer, ForeignKey('interaction_task.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    action_type = Column(String(255))
    timestamp = Column(DateTime)
    details = Column(JSONB)


class SystemResponse(Base):
    __tablename__ = 'system_responses'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    interaction_task_id = Column(Integer, ForeignKey('interaction_task.id'))
    response_type = Column(String(255))
    timestamp = Column(DateTime)
    details = Column(JSONB)


# Child of UserInteraction and parent of UserRequest and SystemResponse
class InteractionTask(Base):
    __tablename__ = 'interaction_task'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_interactions_id = Column(Integer, ForeignKey('user_interactions.id'))

    user_request = relationship('UserRequest')
    system_responses = relationship('SystemResponse')


# Parent table for all user interactions
class UserInteraction(Base):
    __tablename__ = 'user_interactions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    session_name = Column(String(255))
    timestamp = Column(DateTime)

    interaction_task = relationship('InteractionTask', uselist=True)
