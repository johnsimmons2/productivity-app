from flask import Blueprint
from controller.controller import Controller, OK
from service import TransactionService

class TransactionController(Controller):
    transactions = Blueprint('transactions', __name__)

    @transactions.route('/transactions', methods=['GET'])
    def get():
        return OK(TransactionService.getAll())