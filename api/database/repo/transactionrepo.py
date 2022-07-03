from database.repo.dbrepoprovider import DBRepoProvider
from model import Transaction, TransactionTable, Entity
from uuid import uuid4

class TransactionRepo(DBRepoProvider):
    def _getColumnNames(self):
        return TransactionTable.COLUMNS

    def _getTableName(self):
        return TransactionTable.TABLE_NAME

    def _mapColumnsToEntity(self, row: dict) -> Entity:
        return Transaction(
            id=uuid4(),
            amount=row['amount'],
            categoryId=row['categoryId'],
            credit=row['credit'],
            date=row['date'],
            userId=row['userId']
        )

    def _mapEntityToColumns(self, entity: Entity, columns: list) -> list:
        if isinstance(entity, Transaction):
            vals = ['' for _ in range(len(columns))]
            for i, col in enumerate(columns):
                match col:
                    case 'amount': vals[i] = entity.amount
                    case 'credit': vals[i] = entity.credit
                    case 'date': vals[i] = entity.date
                    case 'userId': vals[i] = entity.userId
                    case 'categoryId': vals[i] = entity.categoryId
                    case 'id': vals[i] = entity.id
            return vals