from flask import Flask, render_template, request, url_for, redirect
from maps import app
from maps.forms import LocationForm

@app.route('/', methods=['GET', 'POST'])
def home():
	form = LocationForm(request.form)
	if request.method == 'POST':
		city = request.form['city']
		return redirect(url_for('map', city=request.form['city']))
	else:
		return render_template('index.html', form=form)

@app.route('/<string:city>', methods=['GET', 'POST'])
def map(city):
	return render_template('map.html', city=city)
