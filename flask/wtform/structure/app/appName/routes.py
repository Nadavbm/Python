from flask import Flask, request, render_template, url_for, flash, redirect
from appName import app
from appName.forms import FormTemplate

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
			flash('What? You dont know to write your name???')
	return render_template('index.html', form=form)

