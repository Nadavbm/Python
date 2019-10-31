from wtforms import Form, TextField, StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.orm import model_form
from named.models import Name

NameForm = model_form(Name, base_class=Form)

"""
class NameForm(Form):
	name = StringField('Name', validators=[DataRequired()])
	submit = SubmitField('Submit')
"""

