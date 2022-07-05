from model import User
from database.repo import UserRepo

class UserService:
    repo = UserRepo()

    @classmethod
    def getAll(cls):
        return cls.repo.getAll()
    
    @classmethod
    def get(cls, id: str):
        return cls.repo.get(id)

    @classmethod
    def toUser(cls, row: dict) -> User:
        user: User = cls.repo._mapColumnsToEntity(row)
        return user