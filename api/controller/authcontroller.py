from flask import Blueprint, request
from helper.jwthelper import create_token
from service.authservice import AuthService
from . import OK, UnAuthorized, BadRequest, Posted


auth = Blueprint('auth', __name__)

@auth.route("/auth", methods = ['POST'])
def authenticate():
    if request.data is None:
        return BadRequest('User was not provided or something was wrong with the input fields.')
    authenticated = AuthService.authenticate_user()
    if authenticated is not None:
        return OK(create_token(authenticated))
    else:
        return UnAuthorized()

@auth.route("/auth/register", methods = ['POST'])
def post():
    if request.data is None:
        return BadRequest('No user was provided or the input was invalid.')
    result = AuthService.register_user()
    if result.success:
        return Posted(result)
    else:
        return BadRequest(result)