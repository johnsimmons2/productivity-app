from typing import Tuple
from flask import request
from model import ResultDto

class Controller:
    @staticmethod
    def handle(result: ResultDto, status: str):
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
    def OK(result: ResultDto) -> Tuple:
        return Controller.handle(result, '200 OK')
    
    @staticmethod
    def Posted(result: ResultDto) -> Tuple:
        return Controller.handle(result, '201 POSTED')

OK = Controller.OK
Posted = Controller.Posted