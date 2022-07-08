from controller.controller import OK, UnAuthorized as UNAUTH, BadRequest as BADREQUEST
from flask import Blueprint
from helper.inputhelper import getUser
from helper.jwthelper import createToken
from service import AuthService


auth = Blueprint('auth', __name__)

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