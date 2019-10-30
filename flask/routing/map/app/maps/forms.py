from wtforms import Form, TextField

class LocationForm(Form):
	city = TextField('City')
