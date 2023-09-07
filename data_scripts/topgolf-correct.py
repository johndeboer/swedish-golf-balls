import json

with open('topgolf_locations.json') as source:
    data = json.load(source)

for store in data:
    if 'chain' not in store:
        store['chain'] = 'topgolf'

    if store['lat'] == 0 or store['lon'] == 0:
        print(store['street'] + ' ' + store['city'] + ' ' + store['state'])
        store['lat'] = input('lat:')
        store['lon'] = input('lon:')
        
with open('topgolf_locations.json', 'w') as target:
    json.dump(data, target)