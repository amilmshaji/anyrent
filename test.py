# import geocoder
#
# g = geocoder.ip('me')
#
# print(g.latlng)
# print(g.lat)
# print(g.lng)


from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my_app")

location = geolocator.geocode("kanjirapally")
print(location.latitude, location.longitude)
