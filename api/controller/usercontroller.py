import json
from flask import Blueprint, request
from controller.controller import Controller
from service import UserService, AuthService
OK = Controller.OK
POSTED = Controller.Posted
UNAUTH = Controller.UnAuthorized

class UserController(Controller):
    users = Blueprint('users', __name__)
    
    @users.route("/users", methods = ['GET'])
    def get():
        return OK(UserService.getAll())

    @users.route("/users", methods = ['POST'])
    def post():
        data = json.loads(request.data)
        user = UserService.toUser(data)
        return POSTED(AuthService.registerNewUser(user))

    @users.route("/authenticate", methods = ['POST'])
    def authenticate():
        data = json.loads(request.data)
        user = UserService.toUser(data)
        authenticated = AuthService.authenticateUser(user)
        if authenticated:
            return OK()
        else:
            return UNAUTH()