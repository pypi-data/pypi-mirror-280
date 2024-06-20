import json
from insuant.database import Base
from sqlalchemy import String, Integer, Column, Boolean
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Session
import logging
from typing import TYPE_CHECKING, Dict, Optional
from sqlmodel import JSON, Column, Field, Relationship, SQLModel


class Document(SQLModel, table=True):
    # __tablename__ = 'document'

    id: int = Field(primary_key=True, index=True, default=None, unique=True)
    name: str = Field(index=True, unique=True)
    description: Optional[str] = Field(index=True, nullable=True, default=None)
    doc_summary: Optional[str] = Field(index=True, nullable=True, default=None)
    table_summary: Optional[dict] = Field(default=None, sa_column=Column(JSON))
    texts_4k_token: Optional[str] = Field(default=None, index=False, nullable=True)
    texts: Optional[str] = Field(default=None, index=False, nullable=True)
    tables: Optional[str] = Field(default=None, index=False, nullable=True)
    owner_id: Optional[int] = Field(default=None, index=False, nullable=True)
    is_active: Optional[bool] = Field(default=False, index=False, nullable=True)
    chat_history: Optional[str] = Field(default=None, index=False, nullable=True)

    def __repr__(self):
        return f'<Document {self.name}>'

    @classmethod
    def get_by_name(cls, db: Session, name: str):
        result = db.query(cls).filter(cls.name.ilike(f'%{name}%')).all()
        if result is not None:
            for item in result:
                doc_summary_str = item.doc_summary  # Assuming 'item' is a SQLAlchemy model instance
                try:
                    # Attempt to parse 'doc_summary_str' as JSON
                    doc_summary_json = json.loads(str(doc_summary_str))
                    # Update the tuple with the JSON representation
                    item.doc_summary = doc_summary_json
                except json.JSONDecodeError as e:
                    # Handle the case where the string is not valid JSON
                    print(f"Error decoding JSON: {e}")
        return db.query(cls).filter(cls.name.ilike(f'%{name}%')).all()

    @classmethod
    def get_all(cls, db: Session):
        result = db.query(cls).all()
        if result is not None:
            for item in result:
                doc_summary_str = item.doc_summary  # Assuming 'item' is a SQLAlchemy model instance
                try:
                    # Attempt to parse 'doc_summary_str' as JSON
                    doc_summary_json = json.loads(doc_summary_str)
                    # Update the tuple with the JSON representation
                    item.doc_summary = doc_summary_json
                except json.JSONDecodeError as e:
                    # Handle the case where the string is not valid JSON
                    print(f"Error decoding JSON: {e}")
        return result

    @classmethod
    def get_summary_list(cls, db: Session):
        result = db.query(cls.id, cls.name, cls.doc_summary).all()
        modified_results = []
        if result is not None:
            for item in result:
                doc_summary_str = item.doc_summary  # Assuming 'item' is a SQLAlchemy model instance
                try:
                    # Attempt to parse 'doc_summary_str' as JSON
                    doc_summary_json = json.loads(doc_summary_str)
                    # Update the tuple with the JSON representation
                    # item.doc_summary = doc_summary_json
                    modified_item = {
                        "id": item.id,
                        "name": item.name,
                        "doc_summary": doc_summary_json
                    }
                    # Append the modified item to the list
                    modified_results.append(modified_item)
                except json.JSONDecodeError as e:
                    # Handle the case where the string is not valid JSON
                    print(f"Error decoding JSON: {e}")
        # Convert each row in the result to a dictionary
        # dict_result = [row._asdict() for row in modified_results]

        # Convert the list of dictionaries to a JSON string
        json_str = json.dumps(modified_results)
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
        instance = db.get(cls, id)
        for attr, value in kwargs.items():
            setattr(instance, attr, value)
        db.commit()
        return instance

    @classmethod
    def delete(cls, db: Session, id: int):
        instance = db.get(cls, id)
        db.delete(instance)
        db.commit()

    def toString(self):
        return str(self)
