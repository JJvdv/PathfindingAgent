'''
' Graph Class
' Creates the graph and outgoing edges, as well as loading the weights of each edge
' GetNodes() returns all nodes specified in the node list
' GetOutgoingEdges() returns all edges to a specific node
' Value() returns the weight for the edges of the node
' nodes - Holds all nodes in the graph
' init_graph - Stores the weights of each edge to each node
'''
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = init_graph

    def GetNodes(self):
        return self.nodes

    def GetOutgoingEdges(self, node):
        #print(self.graph[node].keys())
        return list(self.graph[node].keys())

    def Value(self, node1, node2):
        #print(self.graph[node1][node2])
        return self.graph[node1][node2]