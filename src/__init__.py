import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import config
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()    # Database object for SQLAlchemy
migrate = Migrate()  # Database migration object for Flask-Migrate
jwt = JWTManager()

def create_app(config_mode=os.getenv("CONFIG_MODE")):
    app = Flask(__name__)
    app.config.from_object(config[config_mode])  # Load config based on mode

    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    return app
