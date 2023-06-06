import os
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
