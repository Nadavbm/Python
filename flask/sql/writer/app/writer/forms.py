from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class NameForm(FlaskForm):
	name = StringField('Name')
	country = StringField('Country', filters = [lambda x: x or None])
	submit = SubmitField('Submit', filters = [lambda x: x or None])

