import geopy.distance
import geopy.point

import pandas as pd
cities = pd.read_csv('uscities.csv', sep=',', dtype={'lat': float, 'lng': float})

starting_location = {'lat':39.7, 'lng':-104.9}
target_distance = 373

great_circle = []

def takeSecond(elem):
    return elem[0]


for x in range (0,3599):
    gtc = geopy.distance.distance(miles=target_distance).destination((starting_location['lat'],starting_location['lng']), bearing=x/10).format_decimal()
    gtcx, gtcy = map(float, gtc.split(','))
    great_circle.append({'lat': gtcx, 'lng': gtcy, 'bearing': x})

cities_dict = cities.to_dict('records')

def dist(city1, city2):
    return geopy.distance.distance(city1, city2).miles

result_list = []

print(len(great_circle) * len(cities_dict))
n=0
for point in great_circle:
    for city in cities_dict:
        n=n+1
        #if (point['lat'] - city['lat']) < 2 and point['lng'] - city['lng']:
        #calculated_distance = dist(geopy.point.Point(point['lat'],point['lng'],0), geopy.point.Point(city['lat'],city['lng'],0))
        absolute_dist = abs(point['lat'] - city['lat']) + abs(point['lng'] - city['lng'])
        if absolute_dist < .1:
            #print(n, "---", absolute_dist, "---", city['city'])
            result_list.append((absolute_dist, city, point))

result_list.sort(key=lambda y: y[0])

for find in result_list:
    print(find[0],find[1]['city'], find[1]['state_id'], find[1]['population'], find[2]['bearing'])


# list_3 = [ x * y for x in list_1 for y in list_2 ]


#result_list = [dist((city1name, city1state, x1,y1), (city2name, city2state, x2,y2)) for city1name, city1state, x1, y1 in zip(cities['city'], cities['state_id'], cities['lat'], cities['lng'])]

#for result in result_list:
#    print(result)

#print(cities.at[n,'city'] + " --", geopy.distance.distance((cities.at[n,'lat'],cities.at[n,'lng']), (39.747230, -104.992660)).miles)

#for x in range (0,3599):
#    place = geopy.distance.distance(miles=10).destination((39.747230, -104.992660), bearing=x/10).format_decimal()
    #print(place)
