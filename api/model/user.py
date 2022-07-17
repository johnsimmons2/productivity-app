from sqlalchemy import Column, Integer, String, DateTime
# from sqlalchemy.ext.declarative import declarative_base
from model.entity import Entity
from . import db


class User(db.Model, Entity):
    def __init__(self):
        super.__init__(self, type(self))

    __tablename__ = 'users'
    id = db.Column(Integer, primary_key=True)
    guid = Column(String)
    username = Column(String)
    email = Column(String)
    fName = Column(String)
    lName = Column(String)
    # password: str = None
    # salt: str = None
    created = Column(DateTime)
    lastOnline = Column(DateTime)

    # Type hints
    query: db.Query

    def __repr__(self):
        return f"<User(id={self.id}, \
                guid={self.guid}, \
                username={self.username}, \
                name='{self.fName} {self.lName}', \
                email={self.email}"  \
