from flask import render_template, request, redirect, jsonify
from manage import app
from . import main
from .. import db
from .forms import TransactionForm
from ..models import User, Transaction, user_schema, users_schema
import os


@main.route("/user", methods=["POST"])
def add_user():
    # form = TransactionForm()
    # if form.validate_on_submit():

    #Create a User
    username = request.json['username']
    phone_number = request.json['phone_number']

    users = User(username, phone_number)
    db.session.add(users)
    db.session.commit()

    return user_schema.jsonify(users)

@main.route("/transaction", methods=["POST"])
def add_transaction():

    #Create a Transaction
    amount = request.json['amount']
    transacted =request.json['transacted']
    trans_category = request.json['trans_category']
    user_id = request.json['user_id']

    transactions = Transaction(amount, transacted, trans_category, user_id)
    db.session.add(transactions)
    db.session.commit()

    return user_schema.jsonify(transactions)
    
    
    
   