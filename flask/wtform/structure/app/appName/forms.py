from wtforms import Form, TextField, validators, StringField, SubmitField

class FormTemplate(Form):
	name = TextField('Name', validators=[validators.required()]) 
	submit = SubmitField('Submit')


