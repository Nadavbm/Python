from flask import Flask, url_for, render_template, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy
from redirect import app, db
from redirect.models import User 
from redirect.forms import LoginForm

@app.route('/')
@app.route('/home', methods=['GET','POST'])
def home():
	return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if request.method == 'POST':
		user = User(username=form.username.data,email=form.email.data)
		try:
			form.populate_obj(user)
			db.session.add(user)
			db.session.commit()
			return redirect(url_for('view'))
		except:
			print("Something went wrong...")
	return render_template('login.html', form=form)

@app.route('/view', methods=['GET', 'POST'])
def view():
	user = User.query.all()
	return render_template('view.html', user=user)
