from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class LoginForm(FlaskForm):
	username = StringField('Username', filters = [lambda x: x or None])
	email =	StringField('Email', filters = [lambda x: x or None])
	submit = SubmitField('Login', filters = [lambda x: x or None])

