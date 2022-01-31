from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, TextAreaField, SubmitField, DateField, SelectField
from wtforms.validators import Required
from wtforms_sqlalchemy.fields import QuerySelectField
from ..models import User, Transaction, Category

def category_query():
    return Category.query

def user_query():
    return User.query

class TransactionForm(FlaskForm):

    amount = IntegerField("Amount", validators=[Required()] )
    trans_category = SelectField("Category", coerce=int ,validators=[Required()])
    transacted = DateField("Date of Transaction", validators=[Required()] )
    user_id = SelectField("USERID", coerce=int, validators=[Required()] )

    submit =SubmitField("Submit")