from helper.jwthelper import get_access_token
from helper.jwthelper import verify_token
from model.resultdto import ResultDto
from controller import UnAuthorized


def isAuthorized(func):
    def wrapper(*arg, **kwargs) -> ResultDto:
        verified = verify_token(get_access_token())
        if verified:
            return func(*arg, **kwargs)
        else:
            return UnAuthorized('The access token is invalid or expired.')
    wrapper.__name__ = func.__name__
    return wrapper
