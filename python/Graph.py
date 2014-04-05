import sys
from Metro import Metro
from Route import Route

class Graph:
	'''
	A Graph class representing a generic graph that contains nodes and edges.
	'''

	def __init__(self, vertices=None, edges=None):
		'''
		The constructor for the Graph class. It initializes its list of vertices and edges with the given parameters, or empty lists of 
		vertices and edges if no list if provided.
		'''
		self.vertices = vertices or []
		self.edges = edges or []

	def add_vertex(self, vertex):
		'''
		Adds a vertex to the Graph.
		'''
		self.vertices.append(vertex)

	def set_vertices(self, vertices):
		'''
		Sets the list of vertices to the given list of vertices.
		'''
		self.vertices = vertices

	def add_edge(self, vertexACode, vertexBCode, weight):
		'''
		Creates a new Edge object based on the given parameters and adds that Edge to the Graph.
		'''
		ports = [vertexACode, vertexBCode]
		e = Route(ports, weight)
		self.edges.append(e)

	def set_edges(self, edges):
		'''
		Sets the list of edges to the given list of edges.
		'''
		self.edges = edges

	def get_vertex_from_code(self, code):
		'''
		Retrieves the vertex with the given code. If there is no vertex found, then None is returned.
		'''
		for vertex in self.vertices:
			if vertex.code == code:
				return vertex

		return None

	def get_vertex_from_name(self, name):
		'''
		Retrieves the vertex with the given name. If there is no vertex found, then None is returned.
		'''
		for vertex in self.vertices:
			if vertex.name == name:
				return vertex

		return None

	def get_edge(self, vertex_a, vertex_b):
		'''
		Retrieves the edge from vertex_a to vertex_b. If no such vertex was found, then None is returned.
		'''
		for edge in self.edges:
			if vertex_a == edge.ports[0] and vertex_b == edge.ports[1]:
				return edge

		return None

	def shortest_path(self, start, end):
		'''
		Finds the shortest path by distance between those two cities. Returns a stack with the optimal path.
		'''

		optimal_path = {}
		for vertex in self.vertices:
			vertex.tentative_distance = sys.maxint

		unvisited_list = self.vertices[:] # make a shallow copy of the vertices list
		start.tentative_distance = 0
		optimal_path[start] = None

		while unvisited_list: # while there are vertices to visit
			current = min(unvisited_list, key=lambda x: x.tentative_distance)
			unvisited_list.remove(current)
			if current.tentative_distance == sys.maxint or current == end:
				break

			for node in current.outgoing: # update the tentative distances of each vertex
				edge = self.get_edge(current.code, node.code) # get the edge between the two vertices
				if edge is None: # return an empty solution if there's somehow no edge
					return []

				potential_distance = current.tentative_distance + edge.distance
				if node.tentative_distance > potential_distance: # replace the tentative distance with potential distance if the potential distance is smaller
					node.tentative_distance = potential_distance
					optimal_path[node] = current

		shortest_path = []
		current = end
		while current in optimal_path.keys():
			shortest_path.append(current)
			current = optimal_path[current]

		shortest_path.reverse()
		return shortest_path