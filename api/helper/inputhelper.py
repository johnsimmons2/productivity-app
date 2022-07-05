import json
from service import UserService
from extra.logging import Logger


def getUser(data: any):
    result = None
    try:
        data = json.loads(data)
        result = UserService.toUser(data)
    except Exception as e:
        Logger.error('Failed to get input from {0}'.format(str(e)), e)
    return result