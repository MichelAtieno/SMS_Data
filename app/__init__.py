from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .config import config_options
import os


# basedir = os.path.abspath(os.path.dirname(__file__))

#Init db
db = SQLAlchemy()
#Init ma
ma = Marshmallow()

def create_app(config_name):
    app = Flask(__name__)

    #Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
  
    db.init_app(app)
    ma.init_app(app)

    

    return app