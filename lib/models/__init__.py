import sqlite3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///language_app.db")
Session = sessionmaker(bind=engine)
Base = declarative_base()

CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()

from .user import User
from .lesson import Lesson
from .quiz import Quiz

Base.metadata.create_all(engine)
