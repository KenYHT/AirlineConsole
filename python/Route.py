class Route():
	'''
	A Route class that represents a possible route between two cities. The cities are represented by their respective codes, 
	and the distance between both cities is recorded.
	'''
	
	def __init__(self, ports, distance=None):
		'''
		Initializes the Route object with the given city codes and records the distance between the two cities. The distance defaults to 0
		if no distance is specified. 
		'''
		self.ports = ports # An array of size 2, where the first element is the code of the departure city and the second element is the code of the arrival city
		self.distance = distance or 0 # The distance between the two cities

	def set_departure_city(self, city):
		'''
		Sets the departing port of the Route to the provided city if the city is valid. Returns True if the departing port was successfully set, False otherwise.
		'''
		if type(city) is str and city != "":
			self.ports[0] = city
			return True

		return False

	def set_arrival_city(self, city):
		'''
		Sets the incoming port of the Route to the provided city if the city is valid. Returns True if the incoming port was successfully set, False otherwise.
		'''
		if type(city) is str and city != "":
			self.ports[1] = city
			return True

		return False

	def set_distance(self, distance):
		'''
		Sets the distance of the Route to the provided distance if the distance is valid. Returns True if the distance was successfully set, False otherwise.
		'''
		if type(distance) is int and distance >= 0:
			self.distance = distance
			return True

		return False