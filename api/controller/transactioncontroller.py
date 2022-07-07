from flask import Blueprint
from decorator.auth.authdecorators import isAuthorized
from controller.controller import OK
from service import TransactionService


transactions = Blueprint('transactions', __name__)

@transactions.route('/transactions', methods=['GET'])
@isAuthorized
def get():
    return OK(TransactionService.getAll())