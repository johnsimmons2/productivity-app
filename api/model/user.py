from dataclasses import dataclass
import email
from model.entity import Entity

@dataclass
class User(Entity):
    id: str
    username: str
    email: str
    fName: str
    lName: str
    password: str = None
    salt: str = None
    created: str = None
    lastOnline: str = None

class UserTable:
    COLUMNS = [
        'username',
        'email',
        'firstName',
        'lastName',
        'id',
        'password',
        'salt',
        'created',
        'lastOnline'
    ]
    TABLE_NAME = 'users'
