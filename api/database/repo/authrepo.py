from model import User, UserTable, Entity, ResultDto
from database.repo import DBRepoProvider, UserRepo
from config import config
from uuid import uuid4
from extra.logging import Logger
import hashlib

class AuthRepo(DBRepoProvider):
    @classmethod
    def isAuthorized(cls, user: User, secret: str) -> User | None:
        creds: User = cls._getUserCredentials(user.id).entities[0]
        if creds.password == cls._hash_password(secret, creds.salt):
            return UserRepo.get(user.id).asEntity()
    
    @classmethod
    def _hash_password(cls, password: str, salt: str) -> str:
        secret = config('security')
        try:
            sha = hashlib.sha256()
            sha.update(password.encode(encoding = 'UTF-8', errors = 'strict'))
            sha.update(':'.encode(encoding = 'UTF-8'))
            sha.update(salt.encode(encoding = 'UTF-8', errors = 'strict'))
            sha.update(secret['usersecret'].encode(encoding = 'UTF-8', errors = 'strict'))
            return sha.hexdigest()
        except Exception as error:
            Logger.error(error) 
        return None

    @classmethod
    def _getUserCredentials(cls, id: str) -> ResultDto:
        tableName = AuthRepo._getTableName()
        sql = "SELECT password, id, salt FROM public.{0} WHERE id='{1}';".format(tableName, id)
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
            id=str(uuid4()), 
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