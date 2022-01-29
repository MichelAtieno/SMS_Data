from flask import Flask, request, jsonify
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import config_options
import os

# basedir = os.path.abspath(os.path.dirname(__file__))

bootstrap = Bootstrap()
db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_name):

    #Initializing Application
    app = Flask(__name__)

    #Setting up configurations
    app.config.from_object(config_options[config_name])

    #Initializing Flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    

    #Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
