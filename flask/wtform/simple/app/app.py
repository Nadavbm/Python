from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, StringField, SubmitField, validators

app = Flask(__name__)
app.config['SECRET_KEY'] = 'someblablablakey'
app.config.from_object(__name__)

class FormTemplate(Form):
	name = TextField('Name', validators=[validators.required()])

@app.route('/', methods=['GET', 'POST'])
def home():
	form = FormTemplate(request.form)
	if request.method == 'POST':
		name = request.form['name']
		print("Hello %s" % name)
	if form.validate():
		flash('Hello' + name)
	else:
		flash('All fields required!')

		return render_template('index.html', form=form)

if __name__ == "__main__":
	app.run(host='0.0.0.0')
