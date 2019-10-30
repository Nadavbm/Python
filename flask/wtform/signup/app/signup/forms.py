from wtforms import Form, StringField, PasswordField, validators, SelectField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

class SignupForm(Form):
	name = StringField('Name', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email(message='Please enter valid Email address')])
	password = PasswordField('Password', validators=[DataRequired(message='Enter a password'), EqualTo('confirm', message='Passwords doesnt match')]) 
	confirm = PasswordField('Confirm Password') 

