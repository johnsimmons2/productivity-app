from dataclasses import dataclass
from sqlite3 import Date
from model import Entity

@dataclass
class Transaction(Entity):
    amount: float
    categoryId: str
    credit: bool
    date: Date
    userId: str

class TransactionTable:
    COLUMNS = [
        'amount',
        'categoryId',
        'credit',
        'date',
        'id',
        'userId'
    ]

    TABLE_NAME = 'transactions'