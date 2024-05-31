from results import Results
from get_nodes_and_egdes import GetNodesAndEdges
from agent import PathfinderAgent

if __name__ == "__main__":
    agent_diff = input("Choose a difficulty for me to solve: \n1. Easy\n2. Medium\n")

    nodes, edges, start_node, end_node = GetNodesAndEdges(agent_diff)
        
    agent = PathfinderAgent()
    agent.CreateGraph(nodes, edges)

    previous_nodes, shortest_path = agent.ShortestPath(start_node, end_node)
    Results(agent.init_graph, nodes, previous_nodes, shortest_path, start_node, end_node)