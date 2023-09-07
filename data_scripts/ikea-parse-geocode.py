import json
from geopy.geocoders import Nominatim
import time

storeList = []
geolocator = Nominatim(user_agent='swedish-golf-balls')

with open('ikea_locations.txt') as source:
    while True:
        source.readline()
        name = source.readline().strip()
        source.readline()
        street = source.readline().strip()
        source.readline()
        city = source.readline().strip()
        source.readline()
        

        geocode_string = street + ' ' + city
        
        location = geolocator.geocode(geocode_string, timeout=None)
        time.sleep(1.2)

        

        if name == 'None':
            name = city

        if location:
            lat = location.latitude
            lon = location.longitude
        else:
            print('Error on ' + geocode_string)
            lat = 0
            lon = 0

        store = {'chain': 'ikea', 'name': name, 'street': street, 'city': city, 'lat': lat, 'lon': lon}
        storeList.append(store)

        
        if(not source.readline()):
            break

with open('ikea_locations.json', 'w') as target:
    json.dump(storeList, target)