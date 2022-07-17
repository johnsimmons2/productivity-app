from sqlalchemy import String, Float, Boolean, DateTime, Integer
from . import db


class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(Integer, primary_key=True)
    amount = db.Column(Float)
    categoryId = db.Column(Integer)
    credit = db.Column(Boolean)
    date: db.Column(DateTime)
    userId: db.Column(String)

    query: db.Query

    def __repr__(self):
        return f"<Transaction(id={self.id}, \
            amount={self.amount}"