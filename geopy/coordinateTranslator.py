""" 
This script will translate your address to coordinates
You'll need to fill the following fields:
Street name, street number, city, country

This script use geopy - so run:
pip install geopy

Thanks to https://geopy.readthedocs.io/en/latest/
"""

from geopy.geocoders import Nominatim

street = raw_input("Street name: ")
num = raw_input("Street number: ")
city = raw_input("City: ")
country = raw_input("Country: ")

address = "%s street, %s, %s, %s " % (street, num, city, country)

print("The address given is: %s" % address)

geolocator = Nominatim(user_agent="Nadav")
location = geolocator.geocode("%s" % address)

print("The latitude and longtitude are: ")

print((location.latitude, location.longitude))


