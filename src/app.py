from flask import Flask
from src import extensions


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    extensions.init_app(app=app)
    return app
