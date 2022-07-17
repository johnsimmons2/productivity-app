from model.resultdto import ResultDto
from model.user import User
from database.repo.userrepo import UserRepo


class UserService:
    @classmethod
    def getAll(cls):
        return UserRepo.get_all()

    @classmethod
    def get(cls, id: str):
        return UserRepo.get(id)