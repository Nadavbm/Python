from flask import Flask, render_template

app = Flask(__name__)

firma="MySuperCoolCompanyName"

@app.route('/')
def home():
	return render_template('index.html', firma=firma)

@app.route('/about')
def about():
	return render_template('about.html', firma=firma)

@app.route('/contact')
def contact():
	return render_template('contact.html', firma=firma)

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)




