from flask import Flask
from config import config

from .api import configure_api
from .db import db


def create_app(config_name):
    app = Flask('python-flask-api')

    app.config.from_object(config[config_name])

    # configure MongoEngine
    db.init_app(app)

    # Configuracao da API criada em api.py
    configure_api(app)

    return app
