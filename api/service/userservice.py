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
    def post(cls, user: User):
        return cls.repo.insert(user)

    @classmethod
    def toUser(cls, row: dict) -> User:
        return cls.repo._mapColumnsToEntity(row)