from sqlalchemy import Column, Integer, String, ForeignKey
from . import Base

class Quiz(Base):
    __tablename__ = 'quizzes'

    id = Column(Integer, primary_key=True)
    lesson_id = Column(Integer, ForeignKey('lessons.id'))
    question = Column(String, nullable=False)
    correct_answer = Column(String, nullable=False)

    def __repr__(self):
        return f"<Quiz(question='{self.question}')>"
