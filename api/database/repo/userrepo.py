from collections import OrderedDict
from model.user import User, UserTable, Entity
from database.repo import DBRepoProvider
from uuid import uuid4

class UserRepo(DBRepoProvider):
    def get(self, id: str, col: str = 'id'):
        tableName = self._getTableName()
        sql = "SELECT id, \"firstName\", \"lastName\", email, username, created, \"lastOnline\" FROM public.{0} WHERE \"{1}\"='{2}';".format(tableName, col, id)
        return self.execute_command(sql)
    
    def getByEmail(self, email: str):
        return self.get(email, 'email')
    
    def getByUsername(self, username: str):
        return self.get(username, 'username')
    
    def getAll(self):
        tableName = self._getTableName()
        sql = "SELECT id, \"firstName\", \"lastName\", email, username, created, \"lastOnline\" FROM public.{0};".format(tableName)
        return self.execute_command(sql)

    def _getTableName(self):
        return UserTable.TABLE_NAME
    
    def _getColumnNames(self):
        return UserTable.COLUMNS

    def _mapColumnsToEntity(self, row: dict) -> Entity:
        return User(
            id=row['id'] if 'id' in row.keys() else None,
            username=row['username'] if 'username' in row.keys() else None,
            email=row['email'] if 'email' in row.keys() else None,
            fName=row['firstName'] if 'firstName' in row.keys() else None,
            lName=row['lastName'] if 'lastName' in row.keys() else None,
            password=row['password'] if 'password' in row.keys() else None,
            salt=row['salt'] if 'salt' in row.keys() else None,
            created=row['created'] if 'created' in row.keys() else None,
            lastOnline=row['lastOnline'] if 'lastOnline' in row.keys() else None)

    def _mapEntityToColumns(self, data: Entity, cols: list) -> list:
        if isinstance(data, User):
            vals = ['' for _ in range(len(cols))]
            for i, col in enumerate(cols):
                match col:
                    case 'username': vals[i] = data.username
                    case 'firstName': vals[i] = data.fName
                    case 'lastName': vals[i] = data.lName
                    case 'email': vals[i] = data.email
                    case 'id': vals[i] = data.id
                    case 'password': vals[i] = data.password
                    case 'salt': vals[i] = data.salt
                    case 'created': vals[i] = data.created
                    case 'lastOnline': vals[i] = data.lastOnline
            return vals