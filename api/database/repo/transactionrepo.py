from uuid import uuid4
from model.transaction import Transaction
from model.entity import Entity


class TransactionRepo:
    @classmethod
    def get_all(cls):
        return Transaction.query.all()

    @classmethod
    def get(cls, id: str):
        return Transaction.query.filter_by(id=id)