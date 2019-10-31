from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from named.models import Name 
from named.forms import NameForm
from named import app, db

@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('index.html')

@app.route('/view', methods=['GET', 'POST'])
def view():
	named = Name.query.all()
	return render_template('view.html', named=named)

@app.route('/add', methods=['GET', 'POST'])
def add():
	form = NameForm()
	print('Name form created')
	if request.method == 'POST' and form.validate():
		print('Post entered and form validated')
		named = Name(name=form.name.data)
		try:
			print('Trying to add new name to db')
			db.session.add(named)
			print('Add name')
			db.session.commit()
			print('Commit name')
			flash('Added name successfully!')
		except  e:
			print('Exception!!')
			session.rollback()
			print(e)
		return redirect(url_for('view'))
	return render_template('add.html', form=form)


"""
      named = Name.query.filter_by(name=form.name.data).first()


@app.route('/add', methods=['GET','POST'])
def add():
	named = Name.query.filter_by(id=Name.id).first()
	form = NameForm(request.form)
	if request.method == 'POST' and form.validate():
		named.name = Name(name=request.form['name'])
		db.session.add(named)
		try:
			db.session.commit()
			flash("Added named successfully!")
		except  e:
			session.rollback()
			print(e)
		return redurect(url_for('view'))
	return render_template('add.html', form=form)



@app.route('/add', methods=['GET', 'POST'])
def add():
	form = NameForm(request.form)
	if request.method == 'POST' and form.validate():
		named = Name()
		form.populate_obj(named)
		db.session.add(named)
		db.session.commit()
		flash('New named added successfully!')
	else:
		flash('You might forgot to fill a few fields...')
	return render_template('add.html', form=form)


		
		if form.validate_on_submit():
			named = Name(name=form.name.data, street=form.street.data, number=form.number.data, city=form.city.data, country=form.country.data)
			db.session.add(named)
			db.session.commit()
			return redirect(url_for('view'))
		return render_template('add.html', form=form)



	if request.form:
		named = Name(name=request.form.data("name"), street=request.form.data("street"))
		db.session.add(named)
		db.session.commit()
	return render_template('add.html', form=form)


@app.route('/add', methods=['GET', 'POST'])
def add():
	form = NameForm(request.form)
	if request.method == 'POST':
		name = request.form['name']
		street = request.form['street']
		number = request.form['number']
		city = request.form['city']
		country = request.form['country']
		if form.validate():
			#named = Name(name=request.form['name'], street=request.form['street'], number=request.form['number'], city=request.form['city'], country=request.form['country'])
			named = Name(request.form.to_dict())
			db.session.add(named)
			db.session.commit()
			return redirect(url_for('view', named=named))
	return render_template('add.html', form=form)



@app.route('/add', methods=['GET', 'POST'])
def add():
	form = NameForm(request.form)
	if request.method == 'POST':
		name = request.form['name']
		street = request.form['street']
		number = request.form['number']
		city = request.form['city']
		country = request.form['country']
		if form.validate():
			named = Name(name=request.form['name'], street=request.form['street'], number=request.form['number'], city=request.form['city'], country=request.form['country'])
			db.session.add(named)
			db.session.commit()
			return redirect(url_for('view', named=named))
	return render_template('add.html', form=form)


"""

"""
			named = Name(name=form.name.data, street=form.street.data, number=form.number.data, city=form.city.data, country=form.country.data)
			named.name = form.name.data
			named.street = form.street.data
			named.number = form.number.data
			named.city = form.city.data
			named.country = form.country.data
			#form.populate_obj(named)
"""

