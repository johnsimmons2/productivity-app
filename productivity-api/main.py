from flask import Flask
from controller.controller import Controller
from controller.usercontroller import UserController
from controller.transactioncontroller import TransactionController
from service.dbsetupservice import DBSetupService
OK = Controller.OK

app = Flask(__name__)
app.register_blueprint(UserController.users)
app.register_blueprint(TransactionController.transactions)

@app.route("/")
def get():
    return OK('App is running!')


if __name__ == 'main':
    DBSetupService.start()

