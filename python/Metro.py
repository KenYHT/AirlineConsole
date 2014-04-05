import sys

class Metro:
	'''
	A Metro class that represents a city on a route map for CSAir. It contains all the information associated with that city
	'''

	def __init__(self=None, code=None, name=None, country=None, continent=None, timezone=None, coordinates=None, population=None, region=None):
		'''
		The constructor for the Metro class. It initializes the Metro object with all of the passed in parameters
		'''
		self.code = code or 'N/A'
		self.name = name or 'N/A'
		self.country = country or 'N/A'
		self.continent = continent or 'N/A'
		self.timezone = timezone or 9001
		self.coordinates = coordinates or {}
		self.population = population or 0
		self.region = region or 9001
		self.outgoing = []
		self.incoming = []
		self.tentative_distance = sys.maxint # used for calculating dijkstra's
	
	def set_code(self, code):
		'''
		A setter function for a Metro's code. Returns True if the Metro code was successfully set, False otherwise.
		'''
		if type(code) is str and code != "":
			self.code = code
			return True

		print "The code is invalid."
		return False

	def set_name(self, name):
		'''
		A setter function for a Metro's name. Returns True if the Metro name was successfully set, False otherwise.
		'''
		if type(name) is str and name != "":
			self.name = name
			return True

		print "The name is invalid."
		return False

	def set_country(self, country):
		'''
		A setter function for a Metro's country. Returns True if the Metro country was successfully set, False otherwise.
		'''
		if type(country) is str and country != "":
			self.country = country
			return True

		print "The country is invalid."
		return False

	def set_continent(self, continent):
		'''
		A setter function for a Metro's continent. Returns True if the Metro continent was successfully set, False otherwise.
		'''
		if type(continent) is str and continent != "":
			self.continent = continent
			return True

		print "The continent is invalid."
		return False

	def set_timezone(self, timezone):
		'''
		A setter function for a Metro's timezone. Returns True if the Metro timezone was successfully set, False otherwise.
		'''
		if type(timezone) is int:
			self.timezone = timezone
			return True

		print "The timezone is invalid."
		return False

	def set_coordinates(self, latitude, latitude_value, longitude, longitude_value):
		'''
		A setter function for a Metro's cordinates. Returns True if the Metro cordinates was successfully set, False otherwise.
		'''
		if (latitude == 'N' or latitude == 'S') and type(latitude_value) is int and latitude_value >= 0 and latitude_value <= 90 and (longitude == 'W' or longitude == 'E') and type(longitude_value) is int and longitude_value >= 0 and longitude_value <= 90:
			new_coordinate = {latitude: latitude_value, longitude: longitude_value}
			self.coordinates = new_coordinate
			return True

		print "The coordinate is invalid."
		return False

	def set_population(self, population):
		'''
		A setter function for a Metro's population. Returns True if the Metro population was successfully set, False otherwise.
		'''
		if type(population) is int and population >= 0:
			self.population = population
			return True

		print "The population is invalid."
		return False

	def set_region(self, region):
		'''
		A setter function for a Metro's region. Returns True if the Metro region was successfully set, False otherwise.
		'''
		if type(region) is int:
			self.region = region
			return True

		print "The region is invalid."
		return False

	def add_outgoing(self, metro):
		'''
		Adds a metro to the outgoing list of this Metro. If the metro is already in the ougoing list, then it isn't added. Returns True if the Metro was successfully added to the outgoing list, False otherwise.
		'''
		if isinstance(metro, Metro):
			for city in self.incoming:
				if city == metro:
					return False

			self.outgoing.append(metro)
			return True

		return False

	def remove_outgoing(self, metro):
		'''
		Removes a metro to the outgoing list of this Metro. Returns True if the Metro was successfully removed to the 
		outgoing list, False otherwise.
		'''
		try:
			self.outgoing.remove(metro)
			return True
		except ValueError:
			return False

	def add_incoming(self, metro):
		'''
		Adds a metro to the incoming list of this Metro. If the metro is already in the incoming list, then it isn't added. 
		Returns True if the Metro was successfully added to the incoming list, False otherwise.
		'''
		if isinstance(metro, Metro):
			for city in self.incoming:
				if city == metro:
					return False

			self.incoming.append(metro)
			return True

		return False

	def remove_incoming(self, metro):
		'''
		Removes a metro from the incoming list of this Metro. If the metro doesn't exist in the list, then nothing happens.
		Returns True if the Metro was successfully removed from the incoming list, False otherwise.
		'''
		try:
			self.incoming.remove(metro)
			return True
		except ValueError:
			return False