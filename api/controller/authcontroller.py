from controller.controller import Controller, OK, UnAuthorized as UNAUTH, BadRequest as BADREQUEST
from flask import Blueprint, request
from helper import getUser
from service import AuthService

class AuthController(Controller):
    auth = Blueprint('auth', __name__)

    @auth.route("/auth", methods = ['POST'])
    def authenticate():
        user = getUser(request.data)
        if user is None:
            return BADREQUEST('User was not provided or something was wrong with the input fields.')
        authenticated = AuthService.authenticateUser(user)
        if authenticated:
            return OK()
        else:
            return UNAUTH()