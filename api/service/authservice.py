from datetime import date
from model import User, ResultDto
from database.repo import UserRepo, AuthRepo
from uuid import uuid4
from database.repo import UserRepo
from extra.logging import Logger
from config import config
import hashlib

class AuthService:
    userRepo = UserRepo()
    authRepo = AuthRepo()

    @classmethod
    def registerNewUser(cls, user: User):
        if user.password is None:
            Logger.error('No password provided.')
            return ResultDto(errors=['Password was not provided.'])
        user.salt = str(uuid4())
        user.id = str(uuid4())
        user.password = cls._hash_password(user.password, user.salt)
        user.created = date.today()
        user.lastOnline = date.today()
        return UserRepo().insert(user)
    
    @classmethod
    def authenticateUser(cls, user: User):
        secret = user.password # Unencrypted user password handed in via api

        # Get the user, authenticated by email or username.
        if user.email is not None:
            user = cls.userRepo.getByEmail(user.email).entities[0]
        elif user.username is not None:
            user = cls.userRepo.getByUsername(user.email).entities[0]
        else:
            Logger.error('Oopsie daisies')
        user = cls.authRepo.get(user.id).entities[0] # Get Auth info via auth repo from id.

        password = cls._hash_password(secret, user.salt)
        if user.password == password:
            return True
        else:
            return False

    @classmethod
    def _get_user_password(cls, user: User) -> str:
        return cls.repo.getPassword(user)
    
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
    