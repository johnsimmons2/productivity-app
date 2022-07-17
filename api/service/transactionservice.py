from database.repo.transactionrepo import TransactionRepo
from model.transaction import Transaction

class TransactionService:
    repo = TransactionRepo()

    @classmethod
    def getAll(cls):
        return cls.repo.getAll()
    
    @classmethod
    def get(cls, id: str):
        return cls.repo.get(id)

    @classmethod
    def post(cls, tra: Transaction):
        return cls.repo.insert(tra)

    @classmethod
    def toTransaction(cls, row: dict) -> Transaction:
        return cls.repo._mapColumnsToEntity(row)