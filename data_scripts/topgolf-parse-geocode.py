import json
from geopy.geocoders import Nominatim
import time

storeList = []
geolocator = Nominatim(user_agent='swedish-golf-balls')

with open('topgolf_locations.txt') as source:
    while True:
        name = source.readline().rstrip()
        street = source.readline().rstrip()
        city = source.readline().rstrip()
        state = source.readline().rstrip()

        geocode_string = street + ' ' + city + ' ' + state
        
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

        store = {'chain': 'topgolf', 'name': name, 'street': street, 'city': city, 'state': state, 'lat': lat, 'lon': lon}
        storeList.append(store)

        
        if(not source.readline()):
            break

with open('topgolf_locations.json', 'w') as target:
    json.dump(storeList, target)