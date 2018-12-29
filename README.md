# Distance Calculator #

This is a small script that is able to receive a `csv` file with cities and distances between them and then calculate the shortest road between two points.
It uses Dijkstra algorithm for that.

### Usage ###

```python
from lib.DC import DistanceCalculator

# Initialize the distance calculator
dc = DistanceCalculator(cities_file='cities.csv')
shortest_distance = dc.calculate('ORADEA', 'SIBIU')

if shortest_distance:
    cities, total_distance = shortest_distance
    print("{road}".format(road=(" -> ".join(cities))))
    print("Total distance: {total_distance}km".format(total_distance=total_distance))

```

Output:

```text
ORADEA -> CLUJ -> TURDA -> ALBA-IULIA -> SIBIU
Total distance: 335km
```

### Loading your own cities ###

Make sure you modify the file ***`cities.csv`*** and submit it as a parameter to the DistanceCalculator class.

The csv must have values in this format:

```[start_city],[destination_city],[distance]```

The program will automatically link them as a graph and then it will apply the Dijkstra algorithm to find the shortest path between two cities.

### Limitations ###

The Dijkstra algorithm is not the most efficient algorithm to find the shortest path, but it is fine if you
want to learn more about algorithms.
Dijkstra run in **O(|V|^2)**, where V is the number of nodes.

Read more about Dijkstra here: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm