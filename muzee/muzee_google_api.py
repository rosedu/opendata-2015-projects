from geopy import geocoders
import csv
g_api_key = 'AIzaSyB_djldgwM0HGAg7opZpVx5StLQB1KDkQc'

g = geocoders.GoogleV3(g_api_key)

place, (lat, lng) = list(g.geocode("Bucuresti, Sos Kiseleff Pavel nr 1, sector 1", exactly_one=False))[0]
print (lat, lng)
