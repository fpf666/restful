from flask import Flask
from App import settings
from App.ext import init_app
from App.urls import init_api


def create_app(env_name):
    app = Flask(__name__)
    app.config.from_object(settings.env.get(env_name))
    init_app(app=app)
    init_api(app=app)
    return app