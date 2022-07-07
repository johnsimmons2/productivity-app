from datetime import date
from model import User, ResultDto
from database.repo import UserRepo, AuthRepo
from extra.logging import Logger
from uuid import uuid4

class AuthService:
    @classmethod
    def registerNewUser(cls, user: User):
        if user.password is None:
            Logger.error('No password provided.')
            return ResultDto(errors=['Password was not provided.'])
        user.salt = str(uuid4())
        user.id = str(uuid4())
        user.password = AuthRepo._hash_password(user.password, user.salt)
        user.created = date.today()
        user.lastOnline = date.today()
        return UserRepo.insert(user)
    
    @classmethod
    def authenticateUser(cls, user: User) -> User | None:
        secret = user.password # Unencrypted user password handed in via api
        if user.password is None:
            Logger.error('Attempted to authenticate without a provided password')
            return None
        if user.username and not user.email:
            user = UserRepo.getByUsername(user.username).entities[0]
        elif user.email and not user.username:
            user = UserRepo.getByEmail(user.email).entities[0]
        else:
            Logger.error('Attempted to authenticate without email or username provided, or both were provided.')
            return None
        
        return AuthRepo.isAuthorized(user, secret)
    
    @classmethod
    def decrypt(cls, email: str, pas: str) -> str:
        user = UserRepo.getByEmail(email).asEntity()
        user = AuthRepo._getUserCredentials(user.id).asEntity()
        return AuthRepo._hash_password(pas, user.salt)