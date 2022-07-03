import json
from flask import Blueprint, request
from controller.controller import Controller
from service import UserService
OK = Controller.OK
POSTED = Controller.Posted

class UserController(Controller):
    users = Blueprint('users', __name__)
    service = UserService()
    
    @users.route("/users", methods = ['GET'])
    def get():
        return OK(UserService.getAll())

    @users.route("/users", methods = ['POST'])
    def post():
        data = json.loads(request.data)
        user = UserService.toUser(data)
        result = UserService.post(user)
        return POSTED(result)