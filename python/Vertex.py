'''
A Vertex class representing a vertex on a graph
'''
class Vertex:
	'''
	The constructor for the Vertex class, initializes the instance variable based on the given parameters
	'''
	def __init__(self, value=None, label=None):
		self.value = value or ""
		self.label = label or ""
		self.reachable = []

	'''
	Adds a vertex to the adjacency list of this node
	'''
	def add_reachable(self, vertex):
		self.reachable.append(vertex)

	'''
	Sets this node's adjacency list equal to the given adjacency list
	'''
	def set_reachable(self, vertices):
		self.reachable = vertices