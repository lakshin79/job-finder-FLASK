from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(message='Username must be filled'),Length(min=5,max=20,message='Length of username should be more than 5 characters and less than 20 characters')])
    email = StringField('Email',validators=[DataRequired(message='Email must be filled'),Email()])
    password = PasswordField('Password',validators=[DataRequired(message='password must be filled'),Length(min=7,message='Too small')])
    confirm_password = PasswordField('Confirm Password',validators= [DataRequired(message='confirm password must be filled'),EqualTo('password',message='Both password and confirm password must be same')])
    submit =SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=7,max=15)])
    remember = BooleanField('Remember me')
    submit =SubmitField('Login')