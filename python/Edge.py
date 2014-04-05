'''
A generic Edge class that represents an edge on a graph. It contains a pair of vertices, where the first element in the pair is the source
for the edge, and the second element is the sink, if the edge is directed. Otherwise, the elements are the endpoints of the edge.
'''
class Edge:
	'''
	The constructor for the Edge class. It sets the pair of vertices that the edge connects, and the weight of the edge. The weight is 0
	if no weight is given.
	'''
	def __init__(self, vertices, weight=None):
		self.vertices = vertices
		self.weight = weight or 0