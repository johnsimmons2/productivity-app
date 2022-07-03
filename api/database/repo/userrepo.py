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
            email=row['email'],
            fName=row['firstName'],
            lName=row['lastName'],
            salt=row['salt'] if 'salt' in row.keys() else None,
            created=row['created'] if 'created' in row.keys() else None,
            lastOnline=row['lastOnline'] if 'lastOnline' in row.keys() else None)
    
    def get(self, id: str):
        tableName = self._getTableName()
        sql = "SELECT id, \"firstName\", \"lastName\", email, username, salt, created, \"lastOnline\" FROM public.{0} WHERE id='{1}';".format(tableName, id)
        return self.execute_command(sql)
    
    def getByEmail(self, email: str):
        tableName = self._getTableName()
        sql = "SELECT id, \"firstName\", \"lastName\", email, username, salt, created, \"lastOnline\" FROM public.{0} WHERE email='{1}';".format(tableName, email)
        return self.execute_command(sql)
    
    def getAll(self):
        tableName = self._getTableName()
        sql = "SELECT id, \"firstName\", \"lastName\", email, username, salt, created, \"lastOnline\" FROM public.{0};".format(tableName)
        return self.execute_command(sql)

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