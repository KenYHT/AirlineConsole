import unittest
import sys
sys.path.insert(0, '../')
from Metro import Metro

class TestMetro(unittest.TestCase):
	'''
	A unit test suite for the Metro class.
	'''
	
	def setUp(self):
		'''
		Sets up the test suite by creating a new Metro object before every test is ran.
		'''
		self.metro = Metro('a', 'b')
		self.test_metro = Metro('TESTMETRO', 'TEST METRO')
		self.test_city = Metro('TESTCITY', 'TEST CITY')

	def test_constructor(self):
		'''
		Tests the constructor of the Metro class by checking if all the values passed into the constructor
		match all of the object's instance variables
		'''
		self.assertEqual(self.metro.code, 'a')
		self.assertEqual(self.metro.name, 'b')
		self.assertEqual(self.metro.country, 'N/A')
		self.assertEqual(self.metro.continent, 'N/A')
		self.assertEqual(self.metro.timezone, 9001)
		self.assertEqual(self.metro.coordinates, {})
		self.assertEqual(self.metro.population, 0)
		self.assertEqual(self.metro.region, 9001)

	def test_set_code(self):
		'''
		Tests the set_code() function by changing the code of the metro to a valid code first, then attempting
		to change the code to an invalid input. 
		'''
		self.assertEqual(self.metro.set_code('METRO'), True)
		self.assertEqual(self.metro.set_code(1), False)
		self.assertEqual(self.metro.code, 'METRO')

	def test_set_name(self):
		'''
		Tests the set_name() function by changing the name of the metro to a valid name first, then attempting
		to change the name to an invalid input. 
		'''
		self.assertEqual(self.metro.set_name('METRO CITY'), True)
		self.assertEqual(self.metro.set_name(51), False)
		self.assertEqual(self.metro.name, 'METRO CITY')

	def test_set_country(self):
		'''
		Tests the set_country() function by changing the country of the metro to a valid country first, then attempting
		to change the country to an invalid input. 
		'''
		self.assertEqual(self.metro.set_country('METRO COUTNRY'), True)
		self.assertEqual(self.metro.set_country(72), False)
		self.assertEqual(self.metro.country, 'METRO COUTNRY')

	def test_set_continent(self):
		'''
		Tests the set_continent() function by changing the continent of the metro to a valid continent first, then attempting
		to change the continent to an invalid input. 
		'''
		self.assertEqual(self.metro.set_continent('METRO CONTINENT'), True)
		self.assertEqual(self.metro.set_continent([1]), False)
		self.assertEqual(self.metro.continent, 'METRO CONTINENT')

	def test_set_timezone(self):
		'''
		Tests the set_timezone() function by changing the timezone of the metro to a valid timezone first, then attempting
		to change the timezone to an invalid input. 
		'''
		self.assertEqual(self.metro.set_timezone(1024), True)
		self.assertEqual(self.metro.set_timezone("abcde"), False)
		self.assertEqual(self.metro.timezone, 1024)

	def test_set_coordinates(self):
		'''
		Tests the set_coordinates() function by changing the coordinates of the metro to a valid coordinates first, then attempting
		to change the coordinates to an invalid input. 
		'''
		self.assertEqual(self.metro.set_coordinates('S', 24, 'E', 52), True)
		self.assertEqual(self.metro.set_coordinates('E', 105, 2, -5), False)
		self.assertEqual(self.metro.coordinates, {'S': 24, 'E': 52})

	def test_set_population(self):
		'''
		Tests the set_population() function by changing the population of the metro to a valid population first, then attempting
		to change the population to an invalid input. 
		'''
		self.assertEqual(self.metro.set_population(12345678), True)
		self.assertEqual(self.metro.set_population('abcdefg'), False)
		self.assertEqual(self.metro.population, 12345678)

	def test_set_region(self):
		'''
		Tests the set_region() function by changing the region of the metro to a valid region first, then attempting
		to change the region to an invalid input. 
		'''
		self.assertEqual(self.metro.set_region(52), True)
		self.assertEqual(self.metro.set_region('abbbieieeir'), False)
		self.assertEqual(self.metro.region, 52)

	def test_add_outgoing(self):
		'''
		Tests the add_outgoing() function by adding metros to the outgoing list with add_outgoing() and checking if
		those metros have been added to the outgoing list instance variable. Tests for invalid input by checking if
		the invalid input isn't in the outgoing list.
		'''
		self.assertEqual(self.metro.add_outgoing(self.test_city), True)
		self.assertEqual(self.metro.add_outgoing(self.test_metro), True)
		self.assertEqual(self.metro.add_outgoing('CITY'), False)
		self.assertEqual(self.metro.outgoing[0], self.test_city)
		self.assertEqual(self.metro.outgoing[1], self.test_metro)
		self.assertEqual('CITY' not in self.metro.outgoing, True)

	def test_remove_outgoing(self):
		'''
		Tests the remove_outgoing() function by adding metros to the outgoing list, then removing the element that
		was just added. Afterwards, remove_outgoing() is called with invalid inputs, which shouldn't do anything.
		'''
		self.assertEqual(self.metro.add_outgoing(self.test_city), True)
		self.assertEqual(self.metro.remove_outgoing(self.test_city), True)
		self.assertEqual(self.metro.remove_outgoing(self.test_metro), False)
		self.assertEqual(self.metro.remove_outgoing(5), False)
		self.assertEqual(self.test_city not in self.metro.outgoing, True)

	def test_add_incoming(self):
		'''
		Tests the add_incoming() function by adding metros to the outgoing list with add_incoming() and checking if
		those metros have been added to the incoming list instance variable. Tests for invalid input by checking if
		the invalid input isn't in the incoming list.
		'''
		self.assertEqual(self.metro.add_incoming(self.test_city), True)
		self.assertEqual(self.metro.add_incoming(self.test_metro), True)
		self.assertEqual(self.metro.add_incoming('CITY'), False)
		self.assertEqual(self.metro.incoming[0], self.test_city)
		self.assertEqual(self.metro.incoming[1], self.test_metro)
		self.assertEqual('CITY' not in self.metro.incoming, True)

	def test_remove_incoming(self):
		'''
		Tests the remove_incoming() function by adding metros to the incoming list, then removing the element that
		was just added. Afterwards, remove_outgoing() is called with invalid inputs, which shouldn't do anything.
		'''
		self.assertEqual(self.metro.add_incoming(self.test_city), True)
		self.assertEqual(self.metro.remove_incoming(self.test_city), True)
		self.assertEqual(self.metro.remove_incoming(self.test_metro), False)
		self.assertEqual(self.metro.remove_incoming('aaassdeeee'), False)
		self.assertEqual(self.test_city not in self.metro.incoming, True)

# runs the test suite
suite = unittest.TestLoader().loadTestsFromTestCase(TestMetro)
unittest.TextTestRunner(verbosity=2).run(suite)