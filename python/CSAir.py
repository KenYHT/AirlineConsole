import json
import sys
from Graph import Graph
from Metro import Metro
from Route import Route
from Options import Options

class CSAir:
	'''
	A CSAir class containing the logic behind the CSAir program.
	'''	
	
	def __init__(self, url):
		'''
		The constructor for the CSAir class. It loads the data from a JSON file from the given url, then creates a map containing all
		the cities, flights, and the information associated the the cities and flights.
		'''
		json_data = open(url)
		data = json.load(json_data)
		self.map = Graph() 
		self.data_sources = []
		self.load_file('../json/map_data.json')
		self.load_file('../json/map_addon.json')
		self.load_file('../json/saved_map_data.json')
		self.options = Options(self.map)
		self.init_options()
		json_data.close()

	
	def init_options(self):
		'''
		Initializes the list of options. It creates a list of pairs, where the first element in the pair is the string describing the 
		function call, which is the second element of the pair.
		'''
		self.options = [
			["List all cities", self.options.list_cities],
			["List all flights", self.options.list_routes],
			["Look up all flights from a city", self.options.find_routes_from],
			["Look up all flights to a city", self.options.find_routes_to],
			["Look up a city details", self.options.check_city],
			["Check distance between two cities", self.options.find_distance],
			["Check statistics", self.options.check_statistics],
			["See the route map", self.options.generate_flight_map],
			["Remove a city", self.remove_city],
			["Remove a route", self.remove_route],
			["Add a city", self.add_city],
			["Add a route", self.add_route],
			["Edit a city", self.edit_city],
			["Get information about a route", self.options.user_route_information],
			["Find the shortest route between two cities", self.options.find_shortest_route],
			["Save changes", self.save_network_to_disk],
			["Exit", self.exit]
		]

	def init_data_sources(self, data_sources):
		'''
		Stores the data sources by parsing the data from the JSON file.
		'''
		sources = [source for source in data_sources if source not in self.data_sources or not self.data_sources]
		for source in sources:
			self.data_sources.append(source)

	def init_metros(self, metros_data):
		'''
		Initializes the map with cities by parsing the data from the JSON file.
		'''
		metros = [Metro(metro['code'], metro['name'], metro['country'], metro['continent'], metro['timezone'], metro['coordinates'], metro['population'], metro['region']) for metro in metros_data if self.map.get_vertex_from_code(metro['code']) is None]
		for metro in metros:
			self.map.add_vertex(metro)

	def init_routes(self, routes_data):
		'''
		Initializes the map with flights by parsing the data from the JSON file.
		'''
		routes = []
		for route in routes_data:
			if self.map.get_edge(route['ports'][0], route['ports'][1]) is None:
				routes.append(Route(route['ports'], route['distance']))
				reverse_ports = [route['ports'][1], route['ports'][0]]
				routes.append(Route(reverse_ports, route['distance']))
				src = self.map.get_vertex_from_code(route['ports'][0])
				dest = self.map.get_vertex_from_code(route['ports'][1])
				src.add_outgoing(dest)
				src.add_incoming(dest)
				dest.add_outgoing(src)
				dest.add_incoming(src)

		for route in routes:
			self.map.add_edge(route.ports[0], route.ports[1], route.distance)

	def remove_city(self):
		'''
		Removes the city with the inputed city name from the map. All the other cities and routes are updated with the removal.
		True is returned if the removal was successful, otherwise False.
		'''
		city_name = raw_input("\nPlease enter the city you would like to remove.\n")
		metro = self.map.get_vertex_from_name(city_name)
		if metro is None:
			print "There is no city " + city_name + " being serviced by CSAir."
			return False
		else:
			for city in self.map.vertices: # remove the given city from the outgoing and incoming list of all of the other cities
				if metro in city.incoming:
					city.incoming.remove(metro)
				
				if metro in city.outgoing:	
					city.outgoing.remove(metro)

			for route in self.map.edges: # remove any flights containing the city in one of its ports
				if metro.name == route.ports[0] or metro.name == route.ports[1]:
					self.map.edges.remove(route)

			self.map.vertices.remove(metro)
			return True

	def remove_route(self):
		'''
		Removes the route with the inputed city of departure and arrival from the map. All of the cities are updated with the removal.
		True is returned if the removal was successful, otherwise False.
		'''
		departure_city_name = raw_input("\nPlease enter the city of departure.\n")
		arrival_city_name = raw_input("Please enter the city of arrival.\n")
		departure_city = self.map.get_vertex_from_name(departure_city_name)
		arrival_city = self.map.get_vertex_from_name(arrival_city_name)

		if departure_city is None or arrival_city is None:
			print "You have inputed an invalid city(ies)."
		else:
			for route in self.map.edges: # remove the flight with the inputed city of departure and arrival
				if route.ports[0] == departure_city.code and route.ports[1] == arrival_city.code:
					self.map.edges.remove(route)
					departure_city.outgoing.remove(arrival_city)
					arrival_city.incoming.remove(departure_city)
					return True

		return False

	def add_city(self):
		'''
		Adds a city with the inputed parameters. If the parameters are successfully set, then the city is added to the map.
		True is returned if the city was successfully added, otherwise False.
		'''
		city_code = raw_input("\nPlease enter the city's code.\n")
		city_name = raw_input("Please enter the city's name.\n")
		city_country = raw_input("Please enter the country where the city is located.\n")
		city_continent = raw_input("Please enter the continent where the city is located.\n")
		city_timezone = raw_input("Please enter the city's timezone.\n")
		city_latitude = raw_input("Please enter city's latitudinal direction. Put \"N\" for north and \"S\" for south.\n")
		city_latitude_value = raw_input("Please enter angle of the latitude.\n")
		city_longitude = raw_input("Please enter the city's longitudinal direction. Put \"W\" for west and \"E\" for east.\n")
		city_longitude_value = raw_input("Please enter the angle of the longitude.\n")
		city_population = raw_input("Please enter the city's population.\n")
		city_region = raw_input("Please enter the city's region.\n")

		city_timezone = self.convert_to_int(city_timezone)
		city_latitude_value = self.convert_to_int(city_latitude_value)
		city_longitude_value = self.convert_to_int(city_longitude_value)
		city_population = self.convert_to_int(city_population)
		city_region = self.convert_to_int(city_region)

		city = Metro()
		if city.set_code(city_code) and city.set_name(city_name) and city.set_country(city_country) and city.set_continent(city_continent) and city.set_timezone(city_timezone) and city.set_coordinates(city_latitude, city_latitude_value, city_longitude, city_longitude_value) and city.set_population(city_population) and city.set_region(city_region):
			self.map.add_vertex(city)
			print city_name + " has been successfully added."
			return True

		print "You've given invalid inputs."
		return False

	def add_route(self):
		'''
		Adds a route with the inputed departure and arrival city names along with the distance. If the inputs are valid
		and the flight doesn't already exist, then the route is added to the map and the two cities' incoming and outgoing
		lists are updated.
		'''
		departure_city_name = raw_input("\nPlease enter the city of departure.\n")
		arrival_city_name = raw_input("Please enter the city of arrival.\n")
		distance = raw_input("Please enter the distance of the flight.\n")
		departure_city = self.map.get_vertex_from_name(departure_city_name)
		arrival_city = self.map.get_vertex_from_name(arrival_city_name)

		if departure_city is None or arrival_city is None:
			print "You've inputed one or more invalid city(ies)."
		elif type(distance) is not int or int(distance) < 0:
			print "You've inputed an invalid distance"
		else:
			for route in self.map.edges: # check if the route being added already exists
				if route.ports[0] == departure_city.code and route.ports[1] == arrival_city.code:
					print "This flight already exists"
					return False

			self.map.edges.add_edge(departure_city.code, arrival_city.code, int(distance))
			departure_city.add_outgoing(arrival_city)
			arrival_city.add_incoming(departure_city)
			return True

		return False

	def edit_city(self):
		'''
		Edits the information of a city based on the user's input. Nothing is changed if the user inputs are invalid.
		'''
		metro_name = raw_input("\nWhat city would you like to edit?\n")
		metro = self.map.get_vertex_from_name(metro_name)
		if metro is None:
			print metro_name + " is not serviced by CSAir."
		else:
			edit_metro_options = [
				["Edit code", "Please enter the new code of the city.\n", metro.set_code],
				["Edit name", "Please enter the new name of the city.\n", metro.set_name],
				["Edit country", "Please enter the new country of the city.\n", metro.set_country],
				["Edit continent", "Please enter the new continent of the city.\n", metro.set_continent],
				["Edit timezone", "Please enter the new timezone of the city.\n", metro.set_timezone],
				["Edit coordinates", metro.set_coordinates],
				["Edit population", "Please enter the new population of the city.\n", metro.set_population],
				["Edit region", "Please enter the new region of the city.\n", metro.set_region]
			]

			print "What would you like to edit about the city?"
			for i in range(0, len(edit_metro_options)):
				print str(i) + ". " + edit_metro_options[i][0]

			command = raw_input("What would you like to do?\n")
			if self.is_int(command) and int(command) < len(edit_metro_options) and int(command) >= 0:
					command = int(command)
					if command == 5: # changing the coordinates
						city_latitude = raw_input("Please enter city's latitudinal direction. Put \"N\" for north and \"S\" for south.\n")
						city_latitude_value = raw_input("Please enter angle of the latitude.\n")
						city_longitude = raw_input("Please enter the city's longitudinal direction. Put \"W\" for west and \"E\" for east.\n")
						city_longitude_value = raw_input("Please enter the angle of the longitude.\n")
						city_latitude_value = self.convert_to_int(city_latitude_value)
						city_longitude_value = self.convert_to_int(city_longitude_value)
						if edit_metro_options[command][1](city_latitude, city_latitude_value, city_longitude, city_longitude_value):
							print metro.name + " has been successfully edited."
							return True
					else:
						user_input = raw_input(edit_metro_options[command][1])
						if command == 4 or command == 6 or command == 7: # try converting the input to an integer if the function parameter requires an integer
							user_input = self.convert_to_int(user_input)

						prev_code = metro.code
						if edit_metro_options[command][2](user_input):
							if command == 0: # update all of the routes containing the edited city if the code is changed
								for route in self.map.edges:
									if route.ports[0] == prev_code:
										route.ports[0] = metro.code
									elif route.ports[1] == prev_code:
										route.ports[1] = metro.code

							print metro.name + " has been successfully edited."
							return True

			else:
				print "Your input is not between 0 and " + str(len(edit_metro_options) - 1) + "."

		return False

	def exit(self):
		'''
		Exits the program.
		'''
		print "Exiting program. Thanks for choosing CSAir."
		sys.exit()

	def print_options(self):
		'''
		Prints the list of possible commands onto the console.
		'''
		print "\n=============================================="
		for i in range(0, len(self.options)):
			print str(i) + ". " + self.options[i][0]

	def is_int(self, command):
		'''
		Checks if the given parameter is an integer. Returns true if the parameter is an integer, otherwise false is returned.
		Code taken from: http://stackoverflow.com/questions/1265665/python-check-if-a-string-represents-an-int-without-using-try-except
		'''
		try:
			int(command)
			return True
		except ValueError:
			return False

	def convert_to_int(self, value):
		'''
		Converts the given parameter to an integer. If the parameter can't be converted to an integer, then None is returned.
		'''
		try:
			retval = int(value)
			return retval
		except ValueError:
			return None

	def start_program(self):
		'''
		Starts the CSAir program. It prints the options after every input, and executes the command if the input is valid.
		'''
		print "Welcome to CSAir, your base are belong to us."
		while True:
			self.print_options()
			command = raw_input("\nHow may I help you?\n")
			if self.is_int(command) and int(command) < len(self.options) and int(command) >= 0:
				self.options[int(command)][1]()
			else:
				print "Your input is not between 0 and " + str(len(self.options) - 1) + "."

	def save_network_to_disk(self):
		'''
		Saves the data to a JSON file as a dictionary with keys "data sources", "metros", and "routes".
		'''
		data = {}
		for source in self.data_sources:
			if 'data sources' in data.keys(): # check if 'data source' is a key in the dictionary
				data['data sources'].append(source) # add the source to the list of data sources
			else:
				data['data sources'] = [source] # initialize the key to a list containing the source

		for city in self.map.vertices:
			if 'metros' in data.keys(): # check if 'metros' is a key in the dictionary
				data['metros'].append({"code": city.code, "name": city.name, "country": city.country, "continent": city.continent, "timezone": city.timezone, "coordinates": city.coordinates, "population": city.population, "region": city.region})
			else:
				data['metros'] = [{"code": city.code, "name": city.name, "country": city.country, "continent": city.continent, "timezone": city.timezone, "coordinates": city.coordinates, "population": city.population, "region": city.region}]

		for route in self.map.edges:
			if 'routes' in data.keys(): # check if 'metros' is a key in the dictionary
				if {"ports": [route.ports[0], route.ports[1]], "distance": route.distance} not in data['routes'] and {"ports": [route.ports[1], route.ports[0]], "distance": route.distance} not in data['routes']: # prevent dupes
					data['routes'].append({"ports": [route.ports[0], route.ports[1]], "distance": route.distance})
			else:
				data['routes'] = [{"ports": [route.ports[0], route.ports[1]], "distance": route.distance}]

		with open('../json/saved_map_data.json', 'w') as outfile:
			json.dump(data, outfile, indent=4, separators=(' , ', ' : '))

	def load_file(self, url):
		'''
		Loads the JSON file from the given url and adds the data to the map without any duplicates.
		'''
		json_data = open(url)
		data = json.load(json_data)
		self.init_data_sources(data['data sources'])
		self.init_metros(data['metros'])
		self.init_routes(data['routes'])
		json_data.close()