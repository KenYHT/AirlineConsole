import unittest
import sys
sys.path.insert(0, '../')
from Route import Route

class TestRoute(unittest.TestCase):
	'''
	A unit test suite for the Route class.
	'''

	
	def setUp(self):
		'''
		Sets up the test suite by creating new Route objects before every test is ran
		'''
		cityPair = ['CHI', 'TOR']
		metroPair = ['SHA', 'NYC']
		self.routeA = Route(cityPair, 1337)
		self.routeB = Route(metroPair, 9001)

	def test_constructor(self):
		'''
		Tests the constructor of the Route class by checking if all the values passed into the constructor
		match all of the object's instance variables
		'''
		self.assertEqual('CHI', self.routeA.ports[0])
		self.assertEqual('TOR', self.routeA.ports[1])
		self.assertEqual(1337, self.routeA.distance)
		self.assertEqual('SHA', self.routeB.ports[0])
		self.assertEqual('NYC', self.routeB.ports[1])
		self.assertEqual(9001, self.routeB.distance)

	def test_set_departure_city(self):
		'''
		Tests set_departure_city() by changing the departure city of one route and checking if the change
		applied, then attempting to change the departure city to an invalid input (nothing should happen).
		'''
		self.assertEqual(self.routeA.set_departure_city('TES'), True)
		self.assertEqual(self.routeB.set_departure_city({1:'adfhsdfhy'}), False)
		self.assertEqual(self.routeA.ports[0], 'TES')
		self.assertEqual(self.routeB.ports[0], 'SHA')

	def test_set_arrival_city(self):
		'''
		Tests set_arrival_city() by changing the arrival city of one route and checking if the change
		applied, then attempting to change the arrival city to an invalid input (nothing should happen).
		'''
		self.assertEqual(self.routeB.set_arrival_city('TIN'), True)
		self.assertEqual(self.routeA.set_arrival_city(64386), False)
		self.assertEqual(self.routeB.ports[1], 'TIN')
		self.assertEqual(self.routeA.ports[1], 'TOR')

	def test_set_distance(self):
		'''
		Tests set_distance() by changing the distance of one route and checking if the change
		applied, then attempting to change the distance to an invalid input (nothing should happen).
		'''
		self.assertEqual(self.routeA.set_distance(50256), True)
		self.assertEqual(self.routeB.set_distance([1234, 1235]), False)
		self.assertEqual(self.routeA.distance, 50256)
		self.assertEqual(self.routeB.distance, 9001)

# runs the test suite
suite = unittest.TestLoader().loadTestsFromTestCase(TestRoute)
unittest.TextTestRunner(verbosity=2).run(suite)