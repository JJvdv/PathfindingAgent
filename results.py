'''
' Results function is used to take the Agent class output and display it to the user.
' Firstly, the function prints to console the shortest path total count using the weights.
' Secondly, the path traversed by the agent is displayed using matplotlib.
' Thirdly, pygame is used to display which path the agent takes to get to the end node.
'''

import pygame

import matplotlib.pyplot as plt
import networkx as nx

def Results(init_graph, node_list, previous_nodes, shortest_path, start_node, end_node):
    path = []
    node = end_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
    
    path.append(start_node)
    
    print("The shortest path from start to end is {}".format(shortest_path[end_node]))
    
    g = nx.Graph()
    
    for node in node_list:
        g.add_node(node)
    
    for source_node in init_graph:
        for end_node, weight in init_graph[source_node].items():
            g.add_edge(source_node, end_node, weight=weight)
    
    pos = nx.spring_layout(g)
    nx.draw_networkx_nodes(g, pos, node_size=800)
    nx.draw_networkx_labels(g, pos, font_size=10)
    nx.draw_networkx_edges(g, pos, width=1.0, alpha=0.5, arrowstyle="->", arrows=True, arrowsize=20)
    
    path_nodes = list(reversed(path))
    
    for i in range(len(path_nodes) - 1):
        source_node = path_nodes[i]
        target_node = path_nodes[i + 1]
        nx.draw_networkx_edges(g, pos, edgelist=[(source_node, target_node)], width=2.0, alpha=0.5, edge_color="green", arrows=True, arrowstyle="->", arrowsize=15)
    
    edge_labels = nx.get_edge_attributes(g, "weight")
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)
    
    plt.title("Path Taken")
    plt.axis("off")
    plt.show()
    
    # Simulate the graph travelled by the agent
    pygame.init()
    pygame.display.set_caption("Agent Visualization")
    font = pygame.font.SysFont("Arial", 20)
    clock = pygame.time.Clock()  
    screen = pygame.display.set_mode((800, 600))
    
    running = True
    step = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((255, 255, 255))
        
        # Draw Edges
        for edge in g.edges(data=True):
            source_pos = Visualize(pos[edge[0]], (800, 600))
            target_pos = Visualize(pos[edge[1]], (800, 600))
            pygame.draw.line(screen, (0, 0, 0), source_pos, target_pos, 2)
            # Edge Weights
            mid_pos = ((source_pos[0] + target_pos[0]) // 2, (source_pos[1] + target_pos[1]) // 2)
            weight_text = font.render(str(edge[2]["weight"]), True, (0, 0, 0))
            screen.blit(weight_text, mid_pos)
        
        # Draw Nodes
        for node in g.nodes:
            node_pos = Visualize(pos[node], (800, 600))
            pygame.draw.circle(screen, (0, 0, 255), node_pos, 10)
            node_label = font.render(str(node), True, (0, 0, 0))
            screen.blit(node_label, (node_pos[0] - 10, node_pos[1] - 20))
        
        # Animate the path
        if step < len(path) - 1:
            full_path = list(reversed(path))
            color = pygame.Color("green")
            source_node = full_path[step]
            target_node = full_path[step + 1]
            source_pos = Visualize(pos[source_node], (800, 600))
            target_pos = Visualize(pos[target_node], (800, 600))
            pygame.draw.line(screen, color, source_pos, target_pos, 5)
            step += 1
            pygame.display.flip()
            pygame.time.wait(2000)

        pygame.display.flip()
        
        end_path_mess = font.render("The shortest path from start to end is {}".format(shortest_path[target_node]), True, (0, 0, 0))
        screen.blit(end_path_mess, (20, 520))
        pygame.display.flip()
        
        end_path_disp = font.render("->".join(reversed(path)), True, (0, 0, 0))
        screen.blit(end_path_disp, (20, 560))
        pygame.display.flip()
        
        clear_text = font.render("", True, (0, 0, 0))
        screen.blit(clear_text, (0, 0))
        pygame.display.flip()
        clock.tick(60)
        
        
    pygame.quit()
    

'''
' Visualize function
' Takes in the position and screen size for pygame
' Returns where on the screen the graph needs to be drawn
'''

def Visualize(pos, screen_size):
    return int(pos[0] * screen_size[0] * 0.4) + screen_size[0] // 2, int(pos[1] * screen_size[1] * 0.4) + screen_size[1] // 2