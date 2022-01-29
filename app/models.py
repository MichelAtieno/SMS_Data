from . import db, ma
# from werkzeug.security import generate_password_hash,check_password_hash
# from flask_login import UserMixin
from datetime import datetime


class Transaction(db.Model):

    __tablename__ = 'transactions'

    id = db.Column(db.Integer,primary_key = True)
    account_id = db.Column(db.Integer)
    trans_category = db.Column(db.String)
    image_path = db.Column(db.String)
    amount = db.Column(db.Integer)
    transacted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))


    def save_transaction(self):
        db.session.add(self)
        db.session.commit()



    @classmethod
    def clear_transaction(cls):
        Transaction.all_transactions.clear()

    @classmethod
    def get_transaction(cls,id):
        transctions = Transaction.query.filter_by( account_id=id).all()
        return transactions

    def __repr__(self):
        return f"Transaction('{self.transacted}', '{self.amount}', '{self.trans_category}', '{self.user_id}')"

    def __init__(self, amount, transacted, trans_category, user_id):
        self.amount = amount
        self.transacted = transacted
        self.trans_category = trans_category
        self.user_id = user_id


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    phone_number = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

    transactions = db.relationship('Transaction',backref = 'user',lazy = "dynamic")

    def __repr__(self):
        return f"User ('{self.username}', '{self.phone_number}', '{self.id}')"

    def __init__(self, phone_number, username):
        self.phone_number = phone_number
        self.username = username

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'




# from . import db, ma
# from marshmallow import Schema
# from datetime import datetime
     
# class User(db.Model):

#     id = db.Column(db.Integer, primary_key=True)
#     phone_number = db.Column(db.Integer)
#     username = db.Column(db.String(100))

#     transactions = db.relationship("Transaction", backref="account")
  

#     def __repr__(self):
#         return f"User ('{self.username}', '{self.phone_number}', '{self.id}', '{self.transactions.account}')"

#     def __init__(self, phone_number, username):
#         self.phone_number = phone_number
#         self.username = username


# class Transaction(db.Model):

#     id = db.Column(db.Integer, primary_key=True)
#     amount = db.Column(db.Integer)
#     transacted = db.Column(db.DateTime,default=datetime.utcnow) 
#     category = db.Column(db.String(100))

#     account_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    
#     def __repr__(self):
#         return f"Transaction('{self.account_id}', '{self.amount}', '{self.category}', '{self.account_id}')"

#     def __init__(self, amount, transacted, category, account_id):
#         self.amount = amount
#         self.transacted = transacted
#         self.category = category
#         self.account_id = account_id


# #User Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "phone_number", "username")

#Init schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)

#Transaction Schema
class TransactionSchema(ma.Schema):
    class Meta:
        fields = ("amount", "transacted", "category", "account_id")

#Init schema
transaction_schema = TransactionSchema()
transactions_schema = TransactionSchema(many=True)