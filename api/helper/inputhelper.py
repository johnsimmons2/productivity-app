from service import UserService
from extra.logging import Logger
from flask import request
import json


def getUser():
    try:
        return UserService.toUser(json.loads(request.data))
    except Exception as e:
        Logger.error('Failed to get input from {0}'.format(str(e)), e)
    return None