import json
from insuant.database import Base
from sqlalchemy import String, Integer, Column, Boolean
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Session
import logging


class Document(Base):
    __tablename__ = 'document'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, unique=True)
    description = Column(String, index=False)
    doc_summary = Column(JSONB, index=False)
    table_summary = Column(JSONB, index=False)
    texts_4k_token = Column(String, index=False)
    texts = Column(String, index=False)
    tables = Column(String, index=False)
    owner_id = Column(Integer, index=False)
    is_active = Column(Boolean, default=False)
    chat_history = Column(String, index=False)

    def __repr__(self):
        return f'<Document {self.name}>'

    @classmethod
    def get_by_name(cls, db: Session, name: str):
        return db.query(cls).filter(cls.name.ilike(f'%{name}%')).all()

    @classmethod
    def get_all(cls, db: Session):
        return db.query(cls).all()

    @classmethod
    def get_summary_list(cls, db: Session):
        result = db.query(cls.id, cls.name, cls.doc_summary).all()
        # Convert each row in the result to a dictionary
        dict_result = [row._asdict() for row in result]

        # Convert the list of dictionaries to a JSON string
        json_str = json.dumps(dict_result)
        # print("json_result: ", json_str)

        # isColSet = False;
        json_str = {
            "columns": [{"name": "id"}, {"name": "name"}, {"name": "doc_summary"}],
            "rows": json_str
        }

        return json_str

    @classmethod
    def create(cls, db: Session, **kwargs):
        instance = cls(**kwargs)
        db.add(instance)
        db.commit()
        db.refresh(instance)
        logging.info("Inside document create instance:...")
        logging.debug("Inside document create instance:...", instance)

        return instance

    @classmethod
    def update(cls, db: Session, id: int, **kwargs):
        instance = db.query(cls).get(id)
        for attr, value in kwargs.items():
            setattr(instance, attr, value)
        db.commit()
        return instance

    @classmethod
    def delete(cls, db: Session, id: int):
        instance = db.query(cls).get(id)
        db.delete(instance)
        db.commit()

    def toString(self):
        return str(self)
