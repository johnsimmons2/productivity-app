from flask import Flask
from controller import OK, users, auth, transactions
from service.dbsetupservice import DBSetupService
from extra.logging import Logger, FormattedLogHandler

app = Flask(__name__)
app.register_blueprint(auth)
app.register_blueprint(users)
app.register_blueprint(transactions)

@app.route("/")
def get():
    return OK('App is running!')

if __name__ == 'main':
    # Setup log handler for colors
    Logger.config_set_handler(FormattedLogHandler().set_color_dates(True))
    DBSetupService.start()

