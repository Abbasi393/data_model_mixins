import os
import functools
from flask import Flask, session, request, url_for, redirect
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from webapp.models import *

db = SQLAlchemy()


def get_database_url():
    DB_NAME = os.environ.get('DB_NAME')
    DB_HOST = os.environ.get('DB_HOST')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_USER = os.environ.get('DB_USER')

    DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    return DATABASE_URL


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = get_database_url()
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db, render_as_batch=True)
    return app


def get_app_context():
    """
    Function either gets the current flask app or creates a new one.
    :return: (Flask)  A flask application instance
    """
    from flask import current_app

    if current_app:
        return current_app
    else:
        return create_app()


def with_app_context(fn):
    """
    Decorator to wrap a given function in a flask application context.
    """

    # intended for use with zappa event handler functions, making them more analagous to views

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        app = get_app_context()

        with app.app_context():
            return fn(*args, **kwargs)

    return wrapper
