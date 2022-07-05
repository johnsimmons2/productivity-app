import json
from flask import Blueprint, request
from controller.controller import Controller, OK, Posted as POSTED, BadRequest as BADREQUEST
from service import UserService, AuthService
from helper import getUser

class UserController(Controller):
    users = Blueprint('users', __name__)
    
    @users.route("/users", methods = ['GET'])
    def get():
        return OK(UserService.getAll())

    @users.route("/users", methods = ['POST'])
    def post():
        user = getUser(request.data)
        if user is None:
            return BADREQUEST('No user was provided or the input was invalid.')
        result = AuthService.registerNewUser(user)
        if result.success:
            return POSTED(result)
        else:
            return BADREQUEST(result)