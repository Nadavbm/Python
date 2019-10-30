from flask import Flask, redirect, render_template, flash, request, url_for
from signup import app
from signup.forms import SignupForm

@app.route('/signup/<string:name>', methods=['GET', 'POST'])
def profile(name):
	return render_template('profile.html', name=name)

@app.route('/signup/', methods=['GET', 'POST'])
def signup():
	form = SignupForm(request.form)
	if request.method == 'POST':
		name = request.form['name']
		if form.validate():
			return redirect(url_for('profile', name=request.form['name']))
	return render_template('signup.html', form=form)

@app.route('/')
def home():
	return render_template('index.html')


