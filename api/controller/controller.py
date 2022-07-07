from typing import Tuple
from flask import request
from model import ResultDto

@staticmethod
def handle(status: str, result: ResultDto | str = None, success: bool = False):
    if isinstance(result, str) or result is None:
        result = ResultDto(data=result, success=success, statusmessage=status)
    msg = {
        'success': result.success,
        'status': result.statusmessage,
        'request': request.url
    }
    if result.rowcount > 0:
        msg['rowcount'] = result.rowcount
    if result.entities:
        msg['response'] = result.entities
    elif result.data:
        msg['response'] = result.data
    if len(result.errors) > 0:
        msg['response'] = str(result.errors[0]) if len(result.errors) == 1 else str(result.errors)
    return (msg, status)

@staticmethod
def OK(result: ResultDto | str = None) -> Tuple:
    return handle('200 OK', result, True)

@staticmethod
def Posted(result: ResultDto | str = None) -> Tuple:
    return handle('201 POSTED', result, True)

@staticmethod
def UnAuthorized(result: ResultDto | str = None) -> Tuple:
    return handle('401 UNAUTHORIZED', result, False)

@staticmethod
def BadRequest(result: ResultDto | str = None) -> Tuple:
    return handle('400 BAD REQUEST', result, False)