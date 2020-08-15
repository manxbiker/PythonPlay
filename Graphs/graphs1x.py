""" 
A Python program to demonstrate the adjacency 
list representation of the graph 

add the ability to draw/plot the network from here:
https://networkx.github.io/documentation/stable/tutorial.html#drawing-graphs, and
https://www.quora.com/How-do-you-draw-a-graph-from-the-adjacency-matrix-in-Python 
"""
import networkx as nx 
import matplotlib.pyplot as plt 


# A class to represent the adjacency list of the node 
class AdjNode: 
	def __init__(self, data): 
		self.vertex = data 
		self.next = None


# A class to represent a graph. A graph 
# is the list of the adjacency lists. 
# Size of the array will be the no. of the 
# vertices "V" 
class Graph: 
	def __init__(self, vertices): 
		self.V = vertices 
		self.graph = [None] * self.V 

	# Function to add an edge in an undirected graph 
	def add_edge(self, src, dest): 
		# Adding the node to the source node 
		node = AdjNode(dest) 
		node.next = self.graph[src] 
		self.graph[src] = node 

		# Adding the source node to the destination as 
		# it is the undirected graph 
		node = AdjNode(src) 
		node.next = self.graph[dest] 
		self.graph[dest] = node 

	# Function to print the graph 
	def print_graph(self): 
		G = nx.DiGraph() 
		for i in range(self.V): 
			print("Adjacency list of vertex {}\n head".format(i), end="") 
			temp = self.graph[i] 
			while temp: 
				print(" -> {}".format(temp.vertex), end="") 
				G.add_edge(i, temp.vertex)
				temp = temp.next
			print(" \n") 

		G.add_node(5) #add a node with no edges
		nx.draw(G, with_labels = True)
		plt.show()

# Driver program to the above graph class 
if __name__ == "__main__": 
	V = 5
	graph = Graph(V) 
	graph.add_edge(0, 1) 
	graph.add_edge(0, 4) 
	graph.add_edge(1, 2) 
	graph.add_edge(1, 3) 
	graph.add_edge(1, 4) 
	graph.add_edge(2, 3) 
	graph.add_edge(3, 4) 

	graph.print_graph() 

# This code is contributed by Kanav Malhotra 

# x = input()