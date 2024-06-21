from flask import Blueprint, Flask

from .base_algorithm import BaseAlgorithm

analyse_app = Blueprint('analyse', __name__, url_prefix='/analyse')

from .routes import *
from .exception_handle import *


def run(algorithm):
    BaseAlgorithm.add_subclass(algorithm)
    app = Flask(__name__)
    app.register_blueprint(blueprint=analyse_app)
    app.run()
