from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, TextAreaField, SubmitField, SelectField, validators
from wtforms.fields.html5 import DateField
from wtforms.validators import Required, DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
from ..models import User, Transaction, Category

def category_query():
    return Category.query

class TransactionForm(FlaskForm):
    startdate = DateField('Start Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    enddate = DateField('End Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    submit = SubmitField('Submit')

class CategoryForm(FlaskForm):
    startingdate = DateField('Start Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    endingdate = DateField('End Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    trans_category = QuerySelectField("Category", query_factory=category_query ,validators=[Required()])
    submit = SubmitField('Submit')