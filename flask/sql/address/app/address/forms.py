from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddressForm(FlaskForm):
	name = StringField('Name', filters = [lambda x: x or None])
	street = StringField('Street', filters = [lambda x: x or None])
	number = IntegerField('Number', filters = [lambda x: x or None])
	city = StringField('City', filters = [lambda x: x or None])
	country = StringField('Country', filters = [lambda x: x or None])
	submit = SubmitField('Submit', filters = [lambda x: x or None])

