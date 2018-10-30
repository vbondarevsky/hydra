from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Sequence
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DictMixin:
    def dict(self):
        return dict((col, getattr(self, col)) for col in self.__table__.columns.keys())


class Node(Base, DictMixin):
    __tablename__ = "node"

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String(150), nullable=False)
    url = Column(String(1024), nullable=False)

    def __init__(self, name, url):
        self.name = name
        self.url = url

    def __repr__(self):
        return f"<Node({self.id}, {self.name}, {self.url})>"

    @staticmethod
    def add(db, node):
        new_node = Node(**node)
        db.add(new_node)
        db.commit()
        return new_node.dict()

    @staticmethod
    def remove(db, node_id):
        node = db.query(Node).filter_by(id=node_id).first()
        db.delete(node)
        db.commit()

    @staticmethod
    def read(db, node_id=None):
        if node_id:
            return db.query(Node).filter_by(id=node_id).first().dict()
        else:
            return [node.dict() for node in db.query(Node).all()]

    @staticmethod
    def update(db, node):
        updated_node = db.query(Node).filter_by(id=node["id"]).first()
        updated_node.name = node["name"]
        updated_node.url = node["url"]
        db.commit()
        return updated_node.dict()
