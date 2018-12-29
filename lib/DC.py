import csv

class DistanceCalculator(object):
    def __init__(self, cities_file='cities.csv'):
        self.cities_file = cities_file
        self.cities = {}
        self.distances = {}

        self._load_cities()

    def _load_cities(self):
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

        :param start:
        :param goal:
        :return:
        """

        try:
            assert isinstance(start, str)
            assert isinstance(goal, str)

            dist = dict()
            prev = dict()
            unvisited = set()

            graph = self.cities
            for item in graph:
                dist[item] = float('inf')
                prev[item] = None
                unvisited.add(item)

            dist[start] = 0

            while unvisited:
                u = sorted(unvisited, key=lambda x: dist[x])[0]
                unvisited.remove(u)
                if u == goal:
                    break

                for neighbor in graph[u]:
                    alt = dist[u] + self.distances[u][neighbor]
                    if alt < dist[neighbor]:
                        dist[neighbor] = alt
                        prev[neighbor] = u

            s = []
            u = goal
            if prev[u] or u == start:
                while u:
                    s.insert(0, u)
                    u = prev[u]

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