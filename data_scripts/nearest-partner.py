from geopy import distance
import json

with open('topgolf_locations.json') as tg_source:
    topgolf = json.load(tg_source)

with open('ikea_locations.json') as ik_source:
    ikea = json.load(ik_source)

close = 0
total = 0
for ikea_store in ikea:
    nearest_distance = 1000000
    for topgolf_store in topgolf:
        dist = distance.distance((ikea_store['lat'], ikea_store['lon']), (topgolf_store['lat'], topgolf_store['lon'])).miles
        if dist < nearest_distance:
            nearest_distance = dist
            ikea_store['nearest_distance'] = dist
            ikea_store['nearest_lat'] = topgolf_store['lat']
            ikea_store['nearest_lon'] = topgolf_store['lon']

    print('Nearest TopGolf to ' + ikea_store['name'] + ' is ' + str(nearest_distance) + ' miles.')
    if nearest_distance <= 25:
        close += 1
    total += 1

print(str(close) + ' / ' + str(total) + ' stores within 25 miles')


close = 0
total = 0
for topgolf_store in topgolf:
    nearest_distance = 1000000
    for ikea_store in ikea:
        dist = distance.distance((ikea_store['lat'], ikea_store['lon']), (topgolf_store['lat'], topgolf_store['lon'])).miles
        if dist < nearest_distance:
            nearest_distance = dist
            topgolf_store['nearest_distance'] = dist
            topgolf_store['nearest_lat'] = ikea_store['lat']
            topgolf_store['nearest_lon'] = ikea_store['lon']

    print('Nearest IKEA to TopGolf ' + topgolf_store['name'] + ' is ' + str(nearest_distance) + ' miles.')
    if nearest_distance <= 25:
        close += 1
    total += 1

print(str(close) + ' / ' + str(total) + ' stores within 25 miles')

with open('topgolf_locations.json', 'w') as target:
    json.dump(topgolf, target)

with open('ikea_locations.json','w') as target:
    json.dump(ikea, target)