import json

with open('ikea_locations.json') as source:
    data = json.load(source)

for store in data:
    if 'chain' not in store:
        store['chain'] = 'ikea'

    if store['lat'] == 0 or store['lon'] == 0:
        print(store['street'] + ' ' + store['city'])
        store['lat'] = input('lat:')
        store['lon'] = input('lon:')
        
with open('ikea_locations.json', 'w') as target:
    json.dump(data, target)