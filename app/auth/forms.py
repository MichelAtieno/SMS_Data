from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,ValidationError
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    phone_number = StringField('Your Phone Number',validators=[Required()])
    username = StringField('Enter your username',validators = [Required()])
    password = PasswordField('Password',validators = [Required()])
    submit = SubmitField('Sign Up')

    def validate_phone_number(self,data_field):
        if User.query.filter_by(phone_number =data_field.data).first():
                raise ValidationError('There is an account with that phone_number')
    
    def validate_phone(self, phone_number):
        try: 
            p = phonenumbers.parse(phone_number.data)
            if not phonenumbers.is_valid_number(p):
                raise ValueError()
        except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
            raise ValidationError('Invalid phone number')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

class LoginForm(FlaskForm):
    phone_number = StringField('Your Phone Number',validators=[Required()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

    def validate_phone(self, phone_number):
        try: 
            p = phonenumbers.parse(phone_number.data)
            if not phonenumbers.is_valid_number(p):
                raise ValueError()
        except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
            raise ValidationError('Invalid phone number')
