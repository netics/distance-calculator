import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

from lib.DC import DistanceCalculator

# Initialize the distance calculator
dc = DistanceCalculator(cities_file='cities.csv')
shortest_distance = dc.calculate('ORADEA', 'SIBIU')

if shortest_distance:
    cities, total_distance = shortest_distance
    print("{road}".format(road=(" -> ".join(cities))))
    print("Total distance: {total_distance}km".format(total_distance=total_distance))
