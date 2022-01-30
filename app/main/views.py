from flask import render_template, request, redirect, jsonify
from manage import app
from . import main
from .. import db
from .forms import TransactionForm
from ..models import User, Transaction, Category, user_schema, users_schema, transaction_schema, transactions_schema
import os


@main.route("/")
def home():
    all_users = User.get_users()
    all_transactions = Transaction.query.all()
    data = db.session.query(User, Transaction).join(Transaction).all()
    cat_data = db.session.query(Category, Transaction).join(Transaction).all()
   

    # all_categories = Transaction.objects.values('trans_category__name')
    all_categories = Category.query.all()

    return render_template('index.html', all_users=all_users, all_transactions=all_transactions, data=data, cat_data=cat_data, all_categories=all_categories )


@main.route("/cat/<int:id>")
def category(id):
    data = db.session.query(User, Transaction).join(Transaction).all()
    cat_data = db.session.query(Category, Transaction).join(Transaction).all()
    one_category = Category.query.get(id)
    # cat_queryset = Transaction.query.all()
    
    return render_template("category_profile.html", data=data, cat_data=cat_data, one_category=one_category )

@main.route("/profile/<int:id>")
def user_profile(id):
    data = db.session.query(User, Transaction).join(Transaction).all()
    cat_data = db.session.query(Category, Transaction).join(Transaction).all()
    one_user = User.query.get(id)
    # user_queryset = Transaction.query.all()

    return render_template("user_profile.html", data=data, cat_data=cat_data, one_user=one_user)



@main.route("/user", methods=["POST"])
def add_user():
   
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

    return transaction_schema.jsonify(transactions)
    
    
    
   