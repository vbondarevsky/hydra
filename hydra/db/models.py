from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Sequence
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Node(Base):
    __tablename__ = "node"

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String(150), nullable=False)
    url = Column(String(1024), nullable=False)
    user = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)

    def __init__(self, name, url, user, password):
        self.name = name
        self.url = url
        self.user = user
        self.password = password

    def __repr__(self):
        return f"<Node({self.id}, {self.name}, {self.url})>"
