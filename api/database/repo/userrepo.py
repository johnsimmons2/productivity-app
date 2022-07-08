from model.user import User, UserTable, Entity
from database.repo import DBRepoProvider
from uuid import uuid4

class UserRepo(DBRepoProvider):
    @classmethod
    def get(cls, id: str, col: str = 'id'):
        tableName = cls._getTableName()
        sql = "SELECT id, \"firstName\", \"lastName\", email, username, created, \"lastOnline\" FROM public.{0} WHERE \"{1}\"='{2}';".format(tableName, col, id)
        return cls.execute_command(sql)
    
    @classmethod
    def getByEmail(cls, email: str):
        return cls.get(email, 'email')
    
    @classmethod
    def getByUsername(cls, username: str):
        return cls.get(username, 'username')
    
    @classmethod
    def getAll(cls):
        tableName = cls._getTableName()
        sql = "SELECT id, \"firstName\", \"lastName\", email, username, created, \"lastOnline\" FROM public.{0};".format(tableName)
        return cls.execute_command(sql)

    @classmethod
    def _getTableName(cls):
        return UserTable.TABLE_NAME
    
    @classmethod
    def _getColumnNames(cls):
        return UserTable.COLUMNS

    @classmethod
    def _mapColumnsToEntity(cls, row: dict) -> Entity:
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

    @classmethod
    def _mapEntityToColumns(cls, data: Entity, cols: list) -> list:
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