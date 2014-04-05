import unittest
import sys
sys.path.insert(0, '../')
from Graph import Graph
from Metro import Metro
from Route import Route


class TestGraph(unittest.TestCase):
	'''
	A unit test suite for the Graph class.
	'''

	def setUp(self):
		'''
		Sets up the test suite by creating a new graph before every test is ran
		'''
		city_pair = ['CHI', 'TOR']
		metro_pair = ['SHA', 'NYC']
		shorter_route_a = ['CHI', 'TES']
		shorter_route_b = ['TES', 'TOR']
		routes = [Route(city_pair, 1337), Route(metro_pair, 9001), Route(shorter_route_a, 50), Route(shorter_route_b, 100)]
		metros = [Metro('cityCode1', 'cityName1', 'c', 'd', 'e', 'f', 'g', 'h'), Metro('cityCode2', 'cityName2', 'c', 'd', 'e', 'f', 'g', 'h')]
		chi = Metro('CHI', 'Chicago')
		tor = Metro('TOR', 'Toronto')
		tes = Metro('TES', 'Test City')
		chi.outgoing.append(tor)
		chi.outgoing.append(tes)
		tor.incoming.append(chi)
		tor.incoming.append(tes)
		tes.outgoing.append(tor)
		tes.incoming.append(chi)
		metros.append(chi)
		metros.append(tor)
		metros.append(tes)
		self.graph = Graph(metros, routes)

	def test_constructor(self):
		'''
		Tests the constructor of the Graph class by checking if all the values passed into the constructor
		match all of the object's instance variables
		'''
		self.assertEqual('CHI', self.graph.edges[0].ports[0])
		self.assertEqual('TOR', self.graph.edges[0].ports[1])
		self.assertEqual(1337, self.graph.edges[0].distance)
		self.assertEqual('SHA', self.graph.edges[1].ports[0])
		self.assertEqual('NYC', self.graph.edges[1].ports[1])
		self.assertEqual(9001, self.graph.edges[1].distance)
		self.assertEqual(self.graph.vertices[0].code, 'cityCode1')
		self.assertEqual(self.graph.vertices[0].name, 'cityName1')
		self.assertEqual(self.graph.vertices[0].country, 'c')
		self.assertEqual(self.graph.vertices[0].continent, 'd')
		self.assertEqual(self.graph.vertices[0].timezone, 'e')
		self.assertEqual(self.graph.vertices[0].coordinates, 'f')
		self.assertEqual(self.graph.vertices[0].population, 'g')
		self.assertEqual(self.graph.vertices[0].region, 'h')
		self.assertEqual(self.graph.vertices[1].code, 'cityCode2')
		self.assertEqual(self.graph.vertices[1].name, 'cityName2')
		self.assertEqual(self.graph.vertices[1].country, 'c')
		self.assertEqual(self.graph.vertices[1].continent, 'd')
		self.assertEqual(self.graph.vertices[1].timezone, 'e')
		self.assertEqual(self.graph.vertices[1].coordinates, 'f')
		self.assertEqual(self.graph.vertices[1].population, 'g')
		self.assertEqual(self.graph.vertices[1].region, 'h')

	def test_add_vertex(self):
		'''
		Tests the add_vertex() function by adding metros to the vertices list with add_vertex() and checking if
		those metros have been added to the vertices list instance variable.
		'''
		self.graph.add_vertex(Metro('cityCode3', 'cityName3', 'c', 'd', 'e', 'f', 'g', 'h'))
		new_city = self.graph.get_vertex_from_code('cityCode3')
		self.assertEqual(new_city.code, 'cityCode3')
		self.assertEqual(new_city.name, 'cityName3')
		self.assertEqual(new_city.country, 'c')
		self.assertEqual(new_city.continent, 'd')
		self.assertEqual(new_city.timezone, 'e')
		self.assertEqual(new_city.coordinates, 'f')
		self.assertEqual(new_city.population, 'g')
		self.assertEqual(new_city.region, 'h')

	def test_set_vertices(self):
		'''
		Tests the set_vertices() function by initializing a list of metros and setting the vertices list instance variable
		of the Graph object equal to the list we've initialized by calling set_vertices(). Then we iterate through the list and checking if 
		the list consists of the elements of the original vertices list we've initialized. 
		'''
		metros = [Metro('cityCode3', 'cityName3', 'c', 'd', 'e', 'f', 'g', 'h'), Metro('cityCode4', 'cityName4', 'c', 'd', 'e', 'f', 'g', 'h')]
		self.graph.set_vertices(metros)
		self.assertEqual(self.graph.vertices[0].code, 'cityCode3')
		self.assertEqual(self.graph.vertices[0].name, 'cityName3')
		self.assertEqual(self.graph.vertices[0].country, 'c')
		self.assertEqual(self.graph.vertices[0].continent, 'd')
		self.assertEqual(self.graph.vertices[0].timezone, 'e')
		self.assertEqual(self.graph.vertices[0].coordinates, 'f')
		self.assertEqual(self.graph.vertices[0].population, 'g')
		self.assertEqual(self.graph.vertices[0].region, 'h')
		self.assertEqual(self.graph.vertices[1].code, 'cityCode4')
		self.assertEqual(self.graph.vertices[1].name, 'cityName4')
		self.assertEqual(self.graph.vertices[1].country, 'c')
		self.assertEqual(self.graph.vertices[1].continent, 'd')
		self.assertEqual(self.graph.vertices[1].timezone, 'e')
		self.assertEqual(self.graph.vertices[1].coordinates, 'f')
		self.assertEqual(self.graph.vertices[1].population, 'g')
		self.assertEqual(self.graph.vertices[1].region, 'h')

	def test_add_edge(self):
		'''
		Tests the add_edge() function by adding routes to the edges list with add_edge() and checking if
		those routes have been added to the edges list instance variable.
		'''
		self.graph.add_edge('YOL', 'SWA', 420)
		self.assertEqual('YOL', self.graph.edges[4].ports[0])
		self.assertEqual('SWA', self.graph.edges[4].ports[1])
		self.assertEqual(420, self.graph.edges[4].distance)

	def test_set_edges(self):
		'''
		Tests the set_edges() function by initializing a list of edges and setting the edges list instance variable
		of the Route object equal to the list we've initialized by calling set_edges(). Then we iterate through the list and checking if 
		the list consists of the elements of the original edges list we've initialized. 
		'''
		flightPair = ['TES', 'TIN']
		pair = ['GRA', 'PHS']
		routes = [Route(flightPair, 12345), Route(pair, 98765)]
		self.graph.set_edges(routes)
		self.assertEqual('TES', self.graph.edges[0].ports[0])
		self.assertEqual('TIN', self.graph.edges[0].ports[1])
		self.assertEqual(12345, self.graph.edges[0].distance)
		self.assertEqual('GRA', self.graph.edges[1].ports[0])
		self.assertEqual('PHS', self.graph.edges[1].ports[1])
		self.assertEqual(98765, self.graph.edges[1].distance)

	def test_get_vertex_from_code(self):
		'''
		Tests the get_vertex_from_code() function by calling the function with known codes and checking if the retrieved metros are
		equal to their position in the vertices list in the graph.
		'''
		metro = self.graph.get_vertex_from_code('cityCode1')
		city = self.graph.get_vertex_from_code('cityCode2')
		self.assertEqual(metro, self.graph.vertices[0])
		self.assertEqual(city, self.graph.vertices[1])

	def test_get_vertex_from_name(self):
		'''
		Tests the get_vertex_from_name() function by calling the function with known names and checking if the retrieved metros are
		equal to their position in the vertices list in the graph.
		'''
		metro = self.graph.get_vertex_from_name('cityName1')
		city = self.graph.get_vertex_from_name('cityName2')
		self.assertEqual(metro, self.graph.vertices[0])
		self.assertEqual(city, self.graph.vertices[1])

	def test_get_edge(self):
		'''
		Tests the get_edge() function by adding test vertices and edges to the graph, then calling the function and checking if 
		the edge that is returned is the same as the one made in the beginning. Invalid inputs are tested by checking if None
		is returned when invalid codes are inputed.
		'''
		pyt = Metro('PYT', 'Pyt')
		hon = Metro('HON', 'Hon')
		self.graph.add_vertex(pyt)
		self.graph.add_vertex(hon)
		self.graph.add_edge('PYT', 'HON', 510)
		result = self.graph.get_edge(pyt.code, hon.code)
		self.assertEqual(pyt.code, result.ports[0])
		self.assertEqual(hon.code, result.ports[1])
		false_result = self.graph.get_edge('aaa', 'bbb')
		self.assertEqual(false_result, None)

	def test_shortest_path(self):
		'''
		Tests the shortest_path() function getting existing nodes, and checking if the shortest path outputed by the function calling
		is the same as the shortest path of the graph. It also tests for invalid inputs.
		'''
		chi = self.graph.get_vertex_from_name('Chicago')
		tor = self.graph.get_vertex_from_name('Toronto')
		tes = self.graph.get_vertex_from_name('Test City')
		shortest_path_sol = [chi, tes, tor]
		short_path = self.graph.shortest_path(chi, tor)
		self.assertEqual(shortest_path_sol, short_path)
		# invalid_inputs = self.graph.shortest_path(Metro(). Metro('a', 'b'))
		# self.assertEqual(invalid_inputs, [])

# runs the test suite
suite = unittest.TestLoader().loadTestsFromTestCase(TestGraph)
unittest.TextTestRunner(verbosity=2).run(suite)