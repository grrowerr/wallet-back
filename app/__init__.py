from flask import Flask

from app.config.db_config import DBConfig
from app.extensions import migrate, db


def create_app():
    app = Flask(__name__)
    config = DBConfig()
    app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'KEY'
    app.config['LOGGING_LEVEL'] = 'DEBUG'

    db.init_app(app)
    migrate.init_app(app=app, db=db)

    return app


wallet_app= create_app()
logger_app = wallet_app.logger
logger_app.setLevel(20)
