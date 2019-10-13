from geopy.geocoders import Nominatim

def translator():
	address = "%s street, %s, %s, %s " % (street, num, city, country)

	print("The address given is: %s" % address)

	geolocator = Nominatim(user_agent="Nadav")
	location = geolocator.geocode("%s" % address)

	print("The latitude and longtitude are: ")

	print((location.latitude, location.longitude))


