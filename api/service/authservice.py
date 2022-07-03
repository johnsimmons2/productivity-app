from datetime import date
from model import User
from database.repo import UserRepo
from service import UserService
from uuid import uuid4
from database.repo import UserRepo
from extra.logging import Logger
from config import config
import hashlib

class AuthService:
    @classmethod
    def registerNewUser(cls, user: User):
        # TODO: Validate user
        user.salt = str(uuid4())  
        user.password = cls._hash_password(user.password, user.salt)
        user.created = date.today()
        user.lastOnline = date.today()
        return UserRepo().insert(user)
    
    @classmethod
    def authenticateUser(cls, user: User):
        secret = user.password
        user = UserRepo().getByEmail(user.email).entities[0]
        password = cls._hash_password(secret, user.salt)
        if user.password == password:
            return True
        else:
            return False
    
    def _hash_password(password: str, salt: str):
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
    