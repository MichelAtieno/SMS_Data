from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

#Init app
app = Flask(__name__)


#Class/Model
class User(db.Model):
    phone_number = db.Column(db.Integer, primary_key=True)