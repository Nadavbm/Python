from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from address.models import Address 
from address.forms import AddressForm
from address import app, db

@app.route('/', methods=['GET', 'POST'])
def home():
	form = AddressForm()
	if request.method == 'POST':
		address = Address(name=form.name.data,street=form.street.data,number=form.number.data,city=form.city.data,country=form.country.data)
		form.populate_obj(address)
		db.session.add(address)
		db.session.commit()
	data = Address.query.all()
	return render_template('index.html', form=form, data=data)



"""
		person = Person(name=form.name.data,country=form.country.data)
		db.session.add(person)
		db.session.commit() 
	person = Person.query.all()
	return render_template('index.html', form=form, person=person)
"""
