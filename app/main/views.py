from flask import render_template, request, redirect, jsonify
from flask_login import login_user,logout_user,login_required
from manage import app
from . import main
from .. import db
from .forms import TransactionForm
from ..models import User, Transaction, Category, TransactionSchema, CategorySchema, UserSchema
import os


@main.route("/")
@login_required
def home():
    all_users = User.get_users()
    all_transactions = Transaction.query.all()
    data = db.session.query(User, Transaction).join(Transaction).all()
    cat_data = db.session.query(Category, Transaction).join(Transaction).all()
    # all_categories = Transaction.objects.values('trans_category__name')
    all_categories = Category.query.all()

    return render_template('index.html', all_users=all_users, all_transactions=all_transactions, data=data, cat_data=cat_data, all_categories=all_categories )


@main.route("/cat/<int:id>")
@login_required
def category(id):
    # data = db.session.query(User, Transaction).join(Transaction).all()
    # cat_data = db.session.query(Category, Transaction).join(Transaction).all()
    one_category = Category.query.get(id)
    cat_queryset = Transaction.query.all()
    
    return render_template("category_profile.html", one_category=one_category, cat_queryset=cat_queryset )

@main.route("/profile/<int:id>")
@login_required
def user_profile(id):
    # data = db.session.query(User, Transaction).join(Transaction).all()
    # cat_data = db.session.query(Category, Transaction).join(Transaction).all()
    one_user = User.query.get(id)
    user_queryset = Transaction.query.all()

    return render_template("user_profile.html", one_user=one_user, user_queryset=user_queryset)



@main.route("/transactions", methods=["GET"])
@login_required
def get_all_transactions():
    transactions = Transaction.get_all()
    serializer = TransactionSchema(many=True)
    data = serializer.dump(transactions)
    return jsonify(
        data
    )

@main.route("/transactions", methods=["POST"])
@login_required
def create_a_transaction():
    data=request.get_json()
    new_transaction = Transaction(
        amount = data.get("amount"),
        transacted = data.get("transacted"),
        trans_category = data.get("trans_category"),
        user_id = data.get("user_id")
    )
    new_transaction.save()
    serializer = TransactionSchema()
    data = serializer.dump(new_transaction)
    return jsonify(
        data
    ),201



@main.route("/transaction/<int:id>", methods=["GET"])
@login_required
def get_transaction(id):
    transaction=Transaction.query.get(id)
    serializer = TransactionSchema()
    data = serializer.dump(transaction)
    return jsonify(
        data
    ),200

@main.route("/categories", methods=["GET"])
@login_required
def get_all_categories():
    categories = Category.query.all()
    serializer = CategorySchema(many=True)
    data = serializer.dump(categories)
    return jsonify(
        data
    )

@main.route("/categories", methods=["POST"])
@login_required
def create_a_category():
    data=request.get_json()
    new_category = Category(
        name = data.get("name"),
    )
    new_category.save()
    serializer = CategorySchema()
    data = serializer.dump(new_category)
    return jsonify(
        data
    ),201

@main.route("/category/<int:id>", methods=["GET"])
@login_required
def get_category(id):
    one_category = Category.query.get(id)
    category_schema = CategorySchema()
    output = category_schema.dump(one_category)
    return jsonify({'category' : output})

@main.route('/users', methods=["GET"])
@login_required
def get_users():
    all_users = User.query.all()
    user_schema = UserSchema(many=True)
    output = user_schema.dump(all_users)
    return jsonify({'user': output})

@main.route("/user/<int:id>", methods=["GET"])
@login_required
def get_user(id):
    one_user = User.query.get(id)
    user_schema = UserSchema()
    output = user_schema.dump(one_user)
    return jsonify({'user' : output})

@main.route("/users", methods=["POST"])
@login_required
def create_a_user():
    data=request.get_json()
    new_user = User(
        username = data.get("username"),
    )
    new_user.save()
    serializer = UserSchema()
    data = serializer.dump(new_user)
    return jsonify(
        data
    ),201






#     # category=Category.query.get(id)
#     # # cat_queryset=Transaction.query.all()
#     # cat_data = db.session.query(Category, Transaction).join(Transaction).all()
#     # serializer = CategorySchema()
#     # data = serializer.dump(category)

#     return jsonify(
#         data
#     ),200





# @main.route("/transaction/<int:id>", methods=["PUT"])
# def update_transaction(id):
    

# @main.route("/transaction/<int:id>", methods=["DELETE"])
# def delete_transaction(id):
#     pass






# @main.route("/user", methods=["POST"])
# def add_user():
   
#     #Create a User
#     username = request.json['username']
#     phone_number = request.json['phone_number']

#     users = User(username, phone_number)
#     db.session.add(users)
#     db.session.commit()

#     return user_schema.jsonify(users)

# @main.route("/transaction", methods=["POST"])
# def add_transaction():

#     #Create a Transaction
#     amount = request.json['amount']
#     transacted =request.json['transacted']
#     trans_category = request.json['trans_category']
#     user_id = request.json['user_id']

#     transactions = Transaction(amount, transacted, trans_category, user_id)
#     db.session.add(transactions)
#     db.session.commit()

#     return transaction_schema.jsonify(transactions)
    
    
    
   