from . import db
from datetime import datetime

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.Integer, unique=True)
    username = db.Column(db.String(100))

    transactions = db.relationship("Transaction", backref="account", lazy="True")
  

    def __repr__(self):
        return f'User {self.username}'

class Transaction(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    transacted = db.Column(db.DateTime,default=datetime.utcnow) 
    category = db.Column(db.String(100), unique=True)

    account_id = db.Column(db.Integer, db.ForeignKey("user.id"))
   
    def __repr__(self):
        return f"Transaction('{self.account_id}', '{self.amount}', '{self.category}')"
