from flask import Flask
from controller import UserController, TransactionController, OK, AuthController
from service.dbsetupservice import DBSetupService
from extra.logging import Logger, FormattedLogHandler

app = Flask(__name__)
app.register_blueprint(AuthController.auth)
app.register_blueprint(UserController.users)
app.register_blueprint(TransactionController.transactions)

@app.route("/")
def get():
    return OK('App is running!')

if __name__ == 'main':
    # Setup log handler for colors
    Logger.config_set_handler(FormattedLogHandler().set_color_dates(True))
    DBSetupService.start()

