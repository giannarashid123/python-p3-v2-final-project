from sqlalchemy import Column, Integer, String
from . import Base

class Lesson(Base):
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)

    def __repr__(self):
        return f"<Lesson(title='{self.title}')>"
