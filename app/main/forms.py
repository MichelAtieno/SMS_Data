from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, TextAreaField, SubmitField, SelectField, validators
from wtforms.fields.html5 import DateField
from wtforms.validators import Required, DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
from ..models import User, Transaction, Category

# def category_query():
#     return Category.query

# def user_query():
#     return User.query


# class TransactionForm(FlaskForm):

#     amount = IntegerField("Amount", validators=[Required()] )
#     trans_category = QuerySelectField("Category", query_factory=category_query ,validators=[Required()])
#     transacted = DateField("Date of Transaction", validators=[Required()] )
#     user_id = QuerySelectField("USERID", query_factory=user_query, validators=[Required()] )

#     submit =SubmitField("Submit")

class TransactionForm(FlaskForm):
    startdate = DateField('Start Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    enddate = DateField('End Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    submit = SubmitField('Submit')