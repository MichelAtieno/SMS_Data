from flask import render_template, request, redirect, jsonify, url_for, flash, session
from flask_login import login_user,logout_user,login_required, current_user 
from . import main
from .. import db
from .forms import NewTransactionForm, TransactionForm, CategoryForm
from ..models import User, Transaction, Category, TransactionSchema, CategorySchema, UserSchema
import os
from datetime import datetime



@main.route("/",methods=["GET", "POST"])
@login_required
def home():
    all_users = User.get_users()
    all_transactions = Transaction.query.all()
    data = db.session.query(User, Transaction).join(Transaction).all()
    cat_data = db.session.query(Category, Transaction).join(Transaction).all()
    # all_categories = Transaction.objects.values('trans_category__name')
    all_categories = Category.query.all()


    # new_trans_form = NewTransactionForm()
    # if new_trans_form.validate_on_submit():
    #     Transaction.transaction_new_entry(
    #         amount = new_trans_form.amount.data,
    #         trans_category = new_trans_form.trans_category.data,
    #         transacted = new_trans_form.transacted.data,
    #         user_id=current_user.id
           
    #     )
    #     print(type(user_id))
    #     flash('New Transaction Created')
    #     return redirect(url_for('main.home') )

    form = TransactionForm()
    if form.validate_on_submit():
        firstdate = form.startdate.data
        enddate = form.enddate.data
        date_transactions = Transaction.query.filter(Transaction.transacted.between(firstdate, enddate)).all()
        
        session['first_date'] = firstdate
        session['end_date'] = enddate

        return redirect(url_for('main.get_transaction_by_date', firstdate=firstdate, enddate=enddate, transactions=date_transactions))

    cat_form = CategoryForm()
    if cat_form.validate_on_submit():
        startingdate = cat_form.startingdate.data
        endingdate = cat_form.endingdate.data
        category = cat_form.trans_category.data

        date_transactions = Transaction.query.filter(Transaction.transacted.between(startingdate, endingdate)).all()

        session['starting_date'] = startingdate
        session['ending_date'] = endingdate
        
        return redirect(url_for('main.get_category_by_date', startingdate=startingdate, endingdate=endingdate, category=category, transactions=date_transactions, id=category.id))

    return render_template('index.html', all_users=all_users, all_transactions=all_transactions, data=data, cat_data=cat_data, all_categories=all_categories, form=form, cat_form=cat_form)


@main.route("/date/<enddate>&<firstdate>&<transactions>", methods=["GET"])
@login_required
def get_transaction_by_date(enddate, firstdate, transactions):
    firstdate = session.get('first_date')
    enddate = session.get('end_date')
    transactions = Transaction.query.filter(Transaction.transacted.between(firstdate, enddate)).all()

    return render_template('date_transacted.html', firstdate=firstdate, enddate=enddate, transactions=transactions)

@main.route("/category/<startingdate>&<endingdate>&<int:id>", methods=["GET"])
@login_required
def get_category_by_date(startingdate, endingdate, id):
    startingdate = session.get('starting_date')
    endingdate = session.get('ending_date')
    transactions = Transaction.query.filter(Transaction.transacted.between(startingdate, endingdate)).all()
    category = Category.query.get(id)
  
    return render_template('date_category.html', startingdate=startingdate, endingdate=endingdate, transactions=transactions, category=category )


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

@main.route("/transactions", methods=[ "POST"])
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



@main.route("/transactions", methods=["GET"])
@login_required
def get_all_transactions():
    transactions = Transaction.get_all()
    serializer = TransactionSchema(many=True)
    data = serializer.dump(transactions)
    return jsonify(
        data
    )



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
    
    
    
   