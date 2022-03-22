import phonenumbers

# visualise data as a map
import folium

# get location
from phonenumbers import geocoder

# get service provider
from phonenumbers import carrier

# geocoding API service
from opencage.geocoder import OpenCageGeocode

from numbersList import number

API_key = "2334426d41dd484e8cc75d60da1d6e56"
tracked_number = phonenumbers.parse(number)
number_location = geocoder.description_for_valid_number(tracked_number, "en")
provider = phonenumbers.parse(number)
geocoder = OpenCageGeocode(API_key)
query = str(number_location)

# shows all results from geocoding
results = geocoder.geocode(query)

# extrapolate co-ordinates from results
latitude = results[0]['geometry']['lat']
longitude = results[0]['geometry']['lng']

# generate map and markers
theMap = folium.Map(location=[latitude, longitude], zoom_start=10)
folium.Marker([latitude, longitude], popup=number_location).add_to(theMap)
theMap.save("phoneLocation.html")

print("Location:", number_location)
print("Service provider:", carrier.name_for_number(provider, "en"))
print("Co-ordinates:", latitude, longitude)
