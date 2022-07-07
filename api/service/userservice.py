from model import User
from database.repo import UserRepo

class UserService:
    @classmethod
    def getAll(cls):
        return UserRepo.getAll()
    
    @classmethod
    def get(cls, id: str):
        return UserRepo.get(id)

    @classmethod
    def toUser(cls, row: dict) -> User:
        user: User = UserRepo._mapColumnsToEntity(row)
        return user