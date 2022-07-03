from collections import OrderedDict
from model.user import User, UserTable, Entity
from database.repo import DBRepoProvider
from uuid import uuid4

class UserRepo(DBRepoProvider):
    def _getTableName(self):
        return UserTable.TABLE_NAME
    
    def _getColumnNames(self):
        return UserTable.COLUMNS

    def _mapColumnsToEntity(self, row: dict) -> Entity:
        return User(
            id=str(uuid4()), 
            username=row['username'], 
            password=row['password'], 
            email=row['email'],
            fName=row['firstName'],
            lName=row['lastName'])

    def _mapEntityToColumns(self, data: Entity, cols: list) -> list:
        if isinstance(data, User):
            vals = ['' for _ in range(len(cols))]
            for i, col in enumerate(cols):
                match col:
                    case 'password': vals[i] = data.password
                    case 'username': vals[i] = data.username
                    case 'firstName': vals[i] = data.fName
                    case 'lastName': vals[i] = data.lName
                    case 'email': vals[i] = data.email
                    case 'id': vals[i] = data.id
            return vals