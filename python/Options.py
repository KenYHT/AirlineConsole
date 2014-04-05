import webbrowser
import math
from Graph import Graph
from Metro import Metro
from Route import Route

class Options:
	'''
	An Options class that carries out the commands that don't affect CSAir's data for CSAir's program.
	'''

	def __init__(self, flight_map):
		'''
		The constructor for the Options class. It initializes its flight map to the given parameter.
		'''
		self.flight_map = flight_map

	def set_map(self, flight_map):
		'''
		Sets the flight_map of the View to the provided map. Returns True if the map was successfully set, False otherwise.
		'''
		if isinstance(flight_map, Graph):
			self.flight_map = flight_map
			return True

		return False

	def list_cities(self):
		'''
		Prints all the cities that's in CSAir's data.
		'''
		print "\nList of cities serviced by CSAir:"
		for i in range(0, len(self.flight_map.vertices) - 1):
			print self.flight_map.vertices[i].name + ", ",

		print self.flight_map.vertices[len(self.flight_map.vertices) - 1].name

	def list_routes(self):
		'''
		Prints all the flights that's provided by CSAir.
		'''
		print "\nList of all flights serviced by CSAir:"
		for route in self.flight_map.edges:
			print route.ports[0] + " to " + route.ports[1] + ",",

	def find_routes_from(self):
		'''
		Prints all the flights from the inputed city. Returns True if a flight from the city was successfully found, False otherwise.
		'''
		city = raw_input("Please enter the city of departure.\n")
		metro = self.flight_map.get_vertex_from_name(city)
		if metro is None:
			print "You've input an invalid city name."
		else:
			print "\nList of flights departing from " + metro.name + "."
			for destination in metro.outgoing:
				print metro.name + " to " + destination.name # print all the flights

			return True
		return False

	def find_routes_to(self):
		'''
		Prints all flights arriving at the inputed city. Returns True if a flight to the city was successfully found, False otherwise.
		'''
		city = raw_input("Please enter the city of arrival.\n")
		metro = self.flight_map.get_vertex_from_name(city)
		found = False
		if metro is None:
			print "You've input an invalid city name."
		else:
			print "\nList of flights arriving at " + metro.name + "."
			for route in self.flight_map.edges:
				if metro.code == route.ports[1]: # check if there are any flights arriving at that city
					departure = self.flight_map.get_vertex_from_code(route.ports[0])
					found = True
					print departure.name  + " to " + metro.name
			
			if found == True:
				return found
			else:
				print "There are no flights arriving at " + metro.name + "."

		return found

	def check_city(self):
		'''
		Prints all the information relating to the inputted city. Returns True if the inputed city was found on the map, False otherwise.
		'''
		city = raw_input("Please enter the city you wish to check.\n")
		metro = self.flight_map.get_vertex_from_name(city)
		if metro:
			print metro.name + ", code: " + metro.code + ", country: " + metro.country + ", continent: " + metro.continent + ", timezone: " + str(metro.timezone) + ", coordinates: " + str(metro.coordinates) + ", population: " + str(metro.population) + ", region: " + str(metro.region)
			return True

		print str(city) + " isn't serviced by CSAir."
		return False

	def find_distance(self):
		'''
		Prints the distance of the flight between the two inputted cities. Returns True if the distance was successfully calculated from the inputed cities, False otherwise.
		'''
		departure_input = raw_input("Please enter the city of departure.\n")
		arrival_input = raw_input("Please enter the city of arrival.\n")
		departure = self.flight_map.get_vertex_from_name(departure_input)
		arrival = self.flight_map.get_vertex_from_name(arrival_input)
		if arrival and departure:
			for route in self.flight_map.edges:
				if route.ports[0] == departure.code and route.ports[1] == arrival.code:
					print "The distance between " + departure.name + " and " + arrival.name + " is " + str(route.distance) + "."
					return True

		print "There is no existing flight from " + str(departure_input) + " to " + str(arrival_input) + "."
		return False

	def check_statistics(self):
		'''
		Calculates and prints all the statistical information about CSAir's route network.
		'''
		self.calculate_longest_flight()
		self.calculate_shortest_flight()
		self.calculate_average_distance()
		self.calculate_largest_city()
		self.calculate_smallest_city()
		self.calculate_average_population()
		self.calculate_continents()
		self.calculate_hub()

	def calculate_longest_flight(self):
		'''
		Calculates and prints the longest single flight in the network.
		'''
		longest_flight = max(self.flight_map.edges, key=lambda x: x.distance)
		longest_departure = self.flight_map.get_vertex_from_code(longest_flight.ports[0])
		longest_arrival = self.flight_map.get_vertex_from_code(longest_flight.ports[1])
		print "\nThe longest flight is from " + str(longest_departure.name) + " to " + str(longest_arrival.name) + ", and the distance is " + str(longest_flight.distance)  + " kilometers."

	def calculate_shortest_flight(self):
		'''
		Calculates and prints the shortest single flight in the network.
		'''
		shortest_flight = min(self.flight_map.edges, key=lambda x: x.distance)
		shortest_departure = self.flight_map.get_vertex_from_code(shortest_flight.ports[0])
		shortest_arrival = self.flight_map.get_vertex_from_code(shortest_flight.ports[1])
		print "The shortest flight is from " + str(shortest_departure.name) + " to " + str(shortest_arrival.name) + ", and the distance is " + str(shortest_flight.distance)  + " kilometers."

	def calculate_average_distance(self):
		'''
		Calculates and prints the average distance of all the flights in the network.
		'''
		avg_distance = float(sum([int(route.distance) for route in self.flight_map.edges])) / len(self.flight_map.edges)
		print "The average distance among all flights is " + str(avg_distance) + " kilometers."

	def calculate_largest_city(self):
		'''
		Calculates and prints the biggest city (by population) served by CSAir.
		'''
		largest_metro = max(self.flight_map.vertices, key=lambda x: x.population)
		print "The city with the largest population is " + str(largest_metro.name) + " with " + str(largest_metro.population) + " people."

	def calculate_smallest_city(self):
		'''
		Calculates and prints the smallest city (by population) served by CSAir.
		'''
		smallest_metro = min(self.flight_map.vertices, key=lambda x: x.population)
		print "The city with the smallest population is " + str(smallest_metro.name) + " with " + str(smallest_metro.population) + " people."

	def calculate_average_population(self):
		'''
		Calculates and prints the average size (by population) of all the cities served by CSAir
		'''
		avg_population = sum([int(metro.population) for metro in self.flight_map.vertices]) / len(self.flight_map.vertices)
		print "The average population among all flights is " + str(avg_population) + "."

	def calculate_continents(self):
		'''
		Calculates and prints a list of the continents served by CSAir and which cities are in them.
		'''
		continents_dict = {}
		for metro in self.flight_map.vertices:
			continent = str(metro.continent)
			if continent in continents_dict.keys(): # check if the current continent is a key in the dictionary
				continents_dict[continent].append(metro.name) # add the country to the list of countries with the same continent
			else:
				continents_dict[continent] = [metro.name] # initialize the key to a list containing the city

		for continent in continents_dict:
			print "\n" + str(continent) + ": "
			cities = [metro for metro in continents_dict[continent]]
			print ", ".join(cities)

	def calculate_hub(self):
		'''
		Calculates and prints CSAir's hub cities, the cities with the most direct flights.
		'''
		hub = max(self.flight_map.vertices, key=lambda x: len(x.outgoing) + len(x.incoming))
		max_connecting_flights = len(hub.outgoing) + len(hub.incoming)
		hub_cities = filter(lambda x: (len(x.outgoing) + len(x.incoming)) == max_connecting_flights, self.flight_map.vertices)
		print "\nThe hub cities with " + str(max_connecting_flights) + " connections are: "
		hub_names = [metro.name for metro in hub_cities]
		print ", ".join(hub_names)

	def generate_flight_map(self):
		'''
		Generates a url of a flight_map with all the flights serviced by CSAir, then opens the url on a web browser.
		'''
		url = "http://www.gcmap.com/mapui?P="
		for route in self.flight_map.edges:
			url += route.ports[0] + "-" + route.ports[1] + ",+"

		print "\n The url for flight_map containing all the flights is: ", url
		webbrowser.open(url)

	def user_route_information(self):
		'''
		Calculates and prints the total distance of the route, the cost to fly of the route, and the time it will take to travel of 
		the route. Returns True if the statistics were successfully printed, False otherwise.
		'''
		cities = []
		print "Please enter the cities in the route. Enter ! to end the list."
		while True:
			user_input = raw_input("")
			if user_input == '!':
				break
			
			city = self.flight_map.get_vertex_from_name(user_input)
			if city is None:
				print "You've entered an invalid city name."
				return False

			cities.append(city)

		route_list = self.verify_correct_route(cities)
		if route_list is not None:
			total_distance = self.calculate_total_distance(route_list)
			total_cost = self.calculate_cost(route_list)
			total_time = self.calculate_time(route_list, cities)
			print "The total distance is " + str(total_distance) + " kilometers."
			print "The total cost is " + str(total_cost) + " dollars."
			print "The total time is " + str(total_time) + " hours."
			return True

		return False

	def route_information(self, cities):
		'''
		Calculates and prints the total distance of the route, the cost to fly of the route, and the time it will take to travel of 
		the route based on the provided list of cities. Returns True if the statistics were successfully printed, False otherwise.
		'''
		route_list = self.verify_correct_route(cities)
		if route_list is not None:
			total_distance = self.calculate_total_distance(route_list)
			total_cost = self.calculate_cost(route_list)
			total_time = self.calculate_time(route_list, cities)
			print "The total distance is " + str(total_distance) + " kilometers."
			print "The total cost is " + str(total_cost) + " dollars."
			print "The total time is " + str(total_time) + " hours."
			return True

		return False

	def verify_correct_route(self, cities):
		'''
		Checks if the list of cities provided is ordered a way such that there is a flight between each adjacent element in the list.
		A list with all the flights is returned if there is a flight between each adjacent element in the list, None otherwise.
		'''
		if not cities or len(cities) == 1:
			return []

		prev_city = cities[0]
		route_list = []
		for i in range(1, len(cities)):
			found = False
			for route in self.flight_map.edges:
				if prev_city.code == route.ports[0] and cities[i].code == route.ports[1]:
					found = True
					route_list.append(route)

			if not found:
				print "You've entered an invalid path."
				return None
			else:
				prev_city = cities[i]

		return route_list

	def calculate_total_distance(self, route_list):
		'''
		Calculates the total distance covered by the route.
		'''
		total_distance = 0
		for route in route_list:
			total_distance += route.distance

		return total_distance

	def calculate_cost(self, route_list):
		'''
		Calculates the total cost of the route. To calculate cost, the first leg of any flight will cost $0.35 per kilometer traveled. 
		Each additional leg will cost $0.05 less per kilometer. If the cost for a leg of the route becomes free, keep the cost free 
		for the rest of the route. The total cost is returned.
		'''
		total_cost = 0
		cost_per_km = 0.35
		for route in route_list:
			total_cost += route.distance * cost_per_km
			if cost_per_km > 0:
				cost_per_km -= 0.05

		return total_cost

	def calculate_time(self, route_list, cities):
		'''
		Calculates the total time of the route. Each jet spends the first 200 kilometers of its flight uniformly accelerating from 0 kph 
		to 750 kph, stays at 750 kph while it is cruising, and then decelerates uniformly from 750 kph to 0 kph during the last 200 
		kilometers of its flight. If a flight is less than 400 kilometers in distance, the jet accelerates uniformly for the first half 
		of the flight and decelerates uniformly for the second half of the flight. In addition, passengers will experience some layover 
		time while waiting at airports for connecting flights. The schedule to determine the layover time works as follows. The airport 
		with the least number of outbound flights (1) has a layover time of 2 hours. For airports with 2 outbound flights, the layover 
		time is 1hr 50min. Continue subtracting 10 minutes foreach additional outbound flight that CSAir has from an airport to calculate 
		its layover time.
		'''
		total_time = 0
		for route in route_list:
			if route.distance <= 400: 
				acceleration = math.pow(750.0, 2) / route.distance # acceleration = max_velocity squared / 2 * distance
				total_time += 2 * math.sqrt(route.distance / acceleration)
			else:
				acceleration = math.pow(750.0, 2) / 400.0
				total_time += (4 * math.sqrt(route.distance / acceleration)) + ((route.distance - 400) / 750.0)

		if len(route_list) > 1: # only calculate layover if there is a flight to take
			for city in cities:
				layover = (2 - (1 / 6.0 * (len(city.outgoing) - 2)))
				if layover > 0:
					total_time += layover

		return total_time

	def find_shortest_route(self):
		'''
		Gives the shortest path between two cities if the cities are valid and such path exists. The information about the route
		is printed if there is a path. True is returned if there is a shortest path between the two given cities, False otherwise.
		'''
		start = raw_input("\nPlease enter the city at the start of the route.\n")
		end = raw_input("Please enter the city at the end of the route.\n")
		start_city = self.flight_map.get_vertex_from_name(start)
		end_city = self.flight_map.get_vertex_from_name(end)
		if start_city is None or end_city is None:
			print "You've inputed one or more invalid city(ies)."
		else:
			optimal_path = self.flight_map.shortest_path(start_city, end_city)
			if optimal_path:	
				print "The shortest route between " + start + " and " + end + " is :"
				current = [city.name for city in optimal_path]
				print " to ".join(current)
				self.route_information(optimal_path)
				return True
			else:
				print "There is no shortest route from " + start + " and " + end + "."

		return False
