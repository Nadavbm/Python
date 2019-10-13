from flask import Flask, render_template, request
from redis import Redis
from geopy.geocoders import Nominatim

app = Flask(__name__)
redis = Redis(host='redis',port=6379)

@app.route('/')
def index():
    redis.incr('hits')
    return render_template('index.html', visitor=redis.get('hits'))

@app.route('/address',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		address = request.form
		addresstrans = "%s, %s, %s, %s " % ( request.form.get("Street"), request.form.get("Number"), request.form.get("City"), request.form.get("Country"))
		geolocator = Nominatim(user_agent="Nadav")
		location = geolocator.geocode("%s" % addresstrans)
		coordinate = "%.12f', %.12f" % (location.latitude, location.longitude)
		return render_template("result.html",address = address, coordinate = coordinate)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)

