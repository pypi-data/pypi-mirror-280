from insuant.database import Base
from sqlalchemy import String, Integer, Column, Boolean


class Worksheet(Base):
    __tablename__ = 'worksheet'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, index=True)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f'<Worksheet {self.title}>'
