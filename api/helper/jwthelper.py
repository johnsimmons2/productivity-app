from model import User
from config import config
from extra.logging import Logger
from flask import request
import json
import datetime
import jwt


def createToken(user: User) -> str:
    return jwt.encode({'username': user.username, 'email': user.email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, config('security')['jwtsecret'], "HS256")

def verifyToken(token: str) -> bool:
    try:
        result = jwt.decode(token, config('security')['jwtsecret'], "HS256")
        expired = datetime.datetime.utcnow() > datetime.datetime.utcfromtimestamp(result['exp'])
        if expired:
            Logger.warn('JWT Token is expired')
    except Exception as e:
        Logger.error('JWT Token validation failed.', e)
        return False
    return True

def getAccessToken():
    if request.headers and 'Authorization' in request.headers.keys():
        data = request.headers['Authorization']
    elif request.form and 'Authorization' in request.form.keys():
        data = request.form['Authorization']
    elif request.data and request.data['Authorization']:
        data = json.loads(data)
        data = request.data['Authorization']
    else:
        Logger.error('Authorization was not supplied.')
        return None
    try:
        return data.split(' ')[1]
    except Exception:
        Logger.error('Token was not supplied in "Bearer TOKEN" format.')
    return None