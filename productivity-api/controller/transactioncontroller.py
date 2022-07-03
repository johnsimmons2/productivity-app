from flask import Blueprint
from controller.controller import Controller
from service import TransactionService
OK = Controller.OK
Posted = Controller.Posted

class TransactionController(Controller):
    transactions = Blueprint('transactions', __name__)

    @transactions.route('/transactions', methods=['GET'])
    def get():
        return OK(TransactionService.getAll())