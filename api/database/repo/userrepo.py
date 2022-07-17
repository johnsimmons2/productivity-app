from model.user import User


class UserRepo:
    @classmethod
    def get(cls, id: str):
        return User.query.filter_by(id=id)
    
    @classmethod
    def get_all(cls):
        test = User.query.all()
        return test

    @classmethod
    def add(cls, user: User):
        pass