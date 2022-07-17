from flask import Blueprint
from service.userservice import UserService
from decorator.auth.authdecorators import isAuthorized
from . import OK, Posted as POSTED, BadRequest as BADREQUEST
users = Blueprint('users', __name__)


@users.route("/users", methods = ['GET'])
@isAuthorized
def get():
    return OK(UserService.getAll())
