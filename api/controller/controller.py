from typing import Tuple
from flask import request
from model import ResultDto

class Controller:
    @staticmethod
    def handle(status: str, result: ResultDto = None):
        if isinstance(result, str):
            result = ResultDto(data=result, success=True, statusmessage='Online')
        msg = {
            'request': request.url,
            'success': result.success,
            'status': result.statusmessage,
            'count': result.rowcount
        }
        if result.entities:
            msg['response'] = result.entities
        elif result.data:
            msg['response'] = result.data
        elif len(result.errors) > 0:
            msg['response'] = str(result.errors[0]) if len(result.errors) == 1 else str(result.errors)
        return (msg, status)

    @staticmethod
    def OK(result: ResultDto = None) -> Tuple:
        return Controller.handle('200 OK', result)
    
    @staticmethod
    def Posted(result: ResultDto = None) -> Tuple:
        return Controller.handle('201 POSTED', result)

    @staticmethod
    def UnAuthorized(result: ResultDto = None) -> Tuple:
        return Controller.handle('401 UNAUTHORIZED', result)

OK = Controller.OK
Posted = Controller.Posted
UnAuthorized = Controller.UnAuthorized