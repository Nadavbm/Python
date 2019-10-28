from flask import Flask, redirect, render_template, flash, request, url_for
from wtforms import Form, TextField, StringField, SubmitField, validators

app = Flask(__name__)
app.config['SECRET_KEY'] = 'someblablablakey'
app.config.from_object(__name__)

class FormTemplate(Form):
	name = TextField('Name', validators=[validators.required()])

@app.route('/<string:name>')
def profile(name):
	return render_template('profile.html', name=name)

@app.route('/', methods=['GET', 'POST'])
def home():
	form = FormTemplate(request.form)
	if request.method == 'POST':
		name = request.form['name']
		if form.validate():
			return redirect(url_for('profile', name=request.form['name']))
		else:
			flash('All fields required!')
	return render_template('index.html', form=form)

if __name__ == "__main__":
	app.run(host='0.0.0.0')
