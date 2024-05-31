'''
' Agent class - This class initializes the agent.
' Always call CreateGraph() function after creation of agent. As it will create the graphs using the nodes and edges that it is given.
' DijkstraAlgorithm() is used to find the shortest path between the start node and end node.
' ShortestPath() is used to return the shortest path given by the DijkstraAlgorithm and returns previous_node and shortest_path respectively.
' graph - Graph class type to create the graph.
' init_graph - stores each connected edge of the graph and their weights
'''

import sys
from graph_class import Graph

class PathfinderAgent:
    def __init__(self):
        self.graph = None
        self.init_graph = None

    def CreateGraph(self, nodes, edges):
        init_graph = {}
        for node in nodes:
            init_graph[node] = {}
        for edge in edges:
            node1, node2, weight = edge
            init_graph[node1][node2] = weight
        self.graph = Graph(nodes, init_graph)
        self.init_graph = init_graph

    def DijkstraAlgorithm(self, start_node, end_node):
        unvisited_nodes = list(self.graph.GetNodes())
        shortest_path = {}
        previous_nodes = {}
        max_value = sys.maxsize
        
        for node in unvisited_nodes:
            shortest_path[node] = max_value
    
        shortest_path[start_node] = 0
    
        while unvisited_nodes:
            curr_min_node = None
            for node in unvisited_nodes:
                if curr_min_node == None:
                    curr_min_node = node
                elif shortest_path[node] < shortest_path[curr_min_node]:
                    curr_min_node = node
    
            if curr_min_node == end_node:
                break
    
            neighbors = self.graph.GetOutgoingEdges(curr_min_node)
            for ngh in neighbors:
                tentative_val = shortest_path[curr_min_node] + self.graph.Value(curr_min_node, ngh)
                if tentative_val < shortest_path[ngh]:
                    shortest_path[ngh] = tentative_val
                    previous_nodes[ngh] = curr_min_node
    
            unvisited_nodes.remove(curr_min_node)
    
        return previous_nodes, shortest_path

    def ShortestPath(self, start_node, end_node):
        return self.DijkstraAlgorithm(start_node, end_node)