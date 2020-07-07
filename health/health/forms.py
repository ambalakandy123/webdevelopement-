from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, email_validator
from health.models import User 

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min=2,)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):

        user = User.query.filter_by(usernme=username.data).first()
        if user:
            raise ValidationError('The username is already taken.Please try different one.')
    def validate_username(self, email):

        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('The username is already taken.Please try different one.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators =[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')