from flask import Flask

from api.blueprints import resources
from api.ext import config, database


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    database.init_app(app)
    resources.init_app(app)
    return app





