from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from writer.models import Person 
from writer.forms import NameForm
from writer import app, db

@app.route('/', methods=['GET', 'POST'])
def home():
	form = NameForm()
	if request.method == 'POST':
		person = Person(name=form.name.data,country=form.country.data)
		form.populate_obj(person)
		db.session.add(person)
		db.session.commit()
	data = Person.query.all()
	return render_template('index.html', form=form, data=data)



"""
		person = Person(name=form.name.data,country=form.country.data)
		db.session.add(person)
		db.session.commit() 
	person = Person.query.all()
	return render_template('index.html', form=form, person=person)
"""
