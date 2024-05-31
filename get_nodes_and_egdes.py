'''
' Function used to set the values depending on the difficulty of the agent chosen by the user.
' Easy - Has 4 nodes
' Medium - Has 8 nodes, a start and end node needs to be set by the user.
'''
def GetNodesAndEdges(diff):
    if diff == "1" or diff.lower() == "easy":
        nodes = ["Istanbul", "Berlin", "Austria", "Prague"]
        edges = [("Istanbul", "Berlin", 1),
                 ("Berlin", "Austria", 3),
                 ("Austria", "Prague", 5),
                 ("Austria", "Istanbul", 3),
                 ("Berlin", "Prague", 2)]
        start_node = "Istanbul"
        end_node = "Prague"
        
        return nodes, edges, start_node, end_node
    elif diff == "2" or diff.lower() == "medium":
        nodes = ["Uzbekistan", "Copenhagen", "Moscow", "London", "Istanbul", "Berlin", "Austria", "Prague"]
        edges = [("Uzbekistan", "Copenhagen", 5),
                 ("Copenhagen", "Uzbekistan", 5),
                 ("Copenhagen", "Berlin", 1),
                 ("London", "Uzbekistan", 4),
                 ("Copenhagen", "Moscow", 3),
                 ("Moscow", "Austria", 5),
                 ("Moscow", "Prague", 4),
                 ("Austria", "Prague", 1),
                 ("Berlin", "Istanbul", 2),
                 ("Istanbul", "Prague", 2),
                 ("Istanbul", "Copenhagen", 3)]
        
        start_node = input("Where would you like me to start? \nUzbekistan\nBerlin\nAustria\nPrague\nMoscow\nLondon\nCopenhagen\nIstanbul\n")
        end_node = input("Where would you like me to end? {} has been chosen as the starting point\n".format(start_node))
            
        return nodes, edges, start_node, end_node