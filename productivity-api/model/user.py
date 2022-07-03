from dataclasses import dataclass
import email
from model.entity import Entity

@dataclass
class User(Entity):
    username: str
    password: str
    email: str
    fName: str
    lName: str

class UserTable:
    COLUMNS = [
        'username',
        'password',
        'email',
        'firstName',
        'lastName',
        'id'
    ]
    TABLE_NAME = 'users'
