import csv

class DistanceCalculator(object):
    def __init__(self, cities_file='cities.csv'):
        """

        :param cities_file:
        """
        self.cities_file = cities_file
        self.cities = {}
        self.distances = {}

        self._load_cities()

    def _load_cities(self):
        """
        Loads the cities from the CSV file.

        :return:
        """
        cities = {}
        distances = {}
        with open(self.cities_file, 'rb') as cities_file:
            entries = csv.reader(cities_file, delimiter=',')
            for row in entries:
                start, end, distance = row
                distance = int(distance)

                if start not in cities.keys():
                    cities[start] = []
                    distances[start] = dict()

                if end not in cities.keys():
                    cities[end] = []
                    distances[end] = dict()

                cities[start].append(end)
                cities[end].append(start)
                distances[start][end] = distance
                distances[end][start] = distance

        self.cities = cities
        self.distances = distances

    def calculate(self, start, goal):
        """
        Calculates the distance between two cities.

        :param start: starting city
        :param goal: destination city
        :return:
        """

        try:
            # Make sure the user inputs strings as cities
            assert isinstance(start, str)
            assert isinstance(goal, str)

            # Initialize the dictionaries used for the distance, previous city and univisited cities
            dist = dict()
            prev = dict()
            unvisited = set()

            graph = self.cities
            for item in graph:
                # Initialize all the cities with distance=infinity
                dist[item] = float('inf')
                prev[item] = None
                unvisited.add(item)

            # Initialize the starting city with distance=0
            dist[start] = 0

            # Iterate all unvisited cities
            while unvisited:
                # Obtain the city with the lowest distance (in the first case it will be the starting city because it have 0)
                u = sorted(unvisited, key=lambda x: dist[x])[0]

                # Remove the obtained city from unvisited set
                unvisited.remove(u)

                # If the city represents our destination, break the loop
                if u == goal:
                    break

                # Check all the neighbors of the city
                for neighbor in graph[u]:
                    # and see if their distance from the start is lower than the one we already know (in the first case if it is lower than infinity)
                    alt = dist[u] + self.distances[u][neighbor]

                    if alt < dist[neighbor]:
                        # If the distance is lower, update the distance data structure with the new value and store the previous city
                        dist[neighbor] = alt
                        prev[neighbor] = u

            # Here we go in reverse from the goal city to the start city and obtain the road user needs to take between cities
            # (s will represent the road)
            s = []
            u = goal
            if prev[u] or u == start:
                while u:
                    # always insert the city in the beginning of the road (because we are going reverse)
                    s.insert(0, u)
                    u = prev[u]

            # Returns the road and the total distance (using the dictionary dist, we access they key of the goal city - that one
            # contains the distance to it)
            return s, dist[goal]

        except AssertionError as exc:
            print("[ERROR] Make sure you provide valid starting and ending points. Only strings accepted.")
            return False
        except KeyError as exc:
            print("[ERROR] Make sure you provide a valid city name.")
            return False
        except Exception as exc:
            print("[ERROR] Found an error: {exception}".format(exception=exc))
            return False
