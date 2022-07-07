from helper.jwthelper import verifyToken, getAccessToken
from controller.controller import UnAuthorized as UNAUTH
from flask import request
from model import ResultDto

def isAuthorized(func):
    def inner(*arg, **kwargs) -> ResultDto:
        verified = verifyToken(getAccessToken())
        if verified:
            return func(*arg, **kwargs)
        else:
            return UNAUTH('The access token is invalid or expired.')
    return inner