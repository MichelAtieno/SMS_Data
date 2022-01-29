from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class TransactionForm(FlaskForm):

    user = StringField("Account Name", validators=[Required()])
    amount = IntegerField("Amount", validators=[Required()] )
    category = StringField("Category", validators=[Required()])

    submit =SubmitField("Submit")