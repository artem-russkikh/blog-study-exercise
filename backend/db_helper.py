from sqlalchemy import create_engine, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import db_name

engine = create_engine('sqlite:///' + db_name, echo=False)
Session = sessionmaker(bind=engine)

class Post(declarative_base()):
    __tablename__ = 'posts'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String)
    body = Column(String)
    created_at = Column(String)

    def __init__(self, author_id, title, description, body, created_at):
        self.author_id = author_id
        self.title = title
        self.description = description
        self.body = body
        self.created_at = created_at


class User(declarative_base()):
    __tablename__ = 'users'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, nullable=False, unique=True)
    password_encrypted = Column(String, nullable=False)
    token = Column(String, nullable=False, unique=True)

    def __init__(self, email, name, password_encrypted, token):
        self.email = email
        self.name = name
        self.password_encrypted = password_encrypted
        self.token = token
