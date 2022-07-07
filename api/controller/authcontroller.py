from api.service.userservice import UserService
from controller.controller import Controller, OK, UnAuthorized as UNAUTH, BadRequest as BADREQUEST
from flask import Blueprint, request
from helper.inputhelper import getUser
from helper.jwthelper import verifyToken, createToken, getAccessToken
from service import AuthService

class AuthController(Controller):
    auth = Blueprint('auth', __name__)

    # Get Auth (JWT) Token
    @auth.route("/auth", methods = ['POST'])
    def authenticate():
        user = getUser()
        if user is None:
            return BADREQUEST('User was not provided or something was wrong with the input fields.')
        authenticatedUser = AuthService.authenticateUser(user)
        if authenticatedUser is not None:
            return OK(createToken(authenticatedUser))
        else:
            return UNAUTH()
    
    @auth.route('/auth/verify', methods = ['GET', 'POST'])
    def verify():
        token = getAccessToken()
        verified = verifyToken(token)
        if verified:
            return OK()
        else:
            return UNAUTH()