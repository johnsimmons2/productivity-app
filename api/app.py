from flask import Flask
from controller import OK, users, transactions
from service.dbsetupservice import DBSetupService
from extra.logging import Logger, FormattedLogHandler
from sqlalchemy.engine import URL
from config import config
from model.user import User
from model.transaction import Transaction
from model import db

# Create app
app = Flask(__name__)

# Register routes
# app.register_blueprint(auth)
app.register_blueprint(users)
app.register_blueprint(transactions)

# Register db
cfg = config()
uri = URL.create(cfg['drivername'], 
                 cfg['username'], 
                 cfg['password'], 
                 cfg['host'], 
                 cfg['port'], 
                 cfg['database'])
app.config['SQLALCHEMY_DATABASE_URI'] = uri
db.app = app
db.init_app(app)
db.create_all()
# Startup
if __name__ == 'main':
    # Setup log handler for colors
    Logger.config_set_handler(FormattedLogHandler().set_color_dates(True))
    DBSetupService.start()

