from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import config

db = SQLAlchemy()    # Database object for SQLAlchemy
migrate = Migrate()  # Database migration object for Flask-Migrate

def create_app(config_mode="development"):
    app = Flask(__name__)
    app.config.from_object(config[config_mode])  # Load config based on mode

    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)

    return app
