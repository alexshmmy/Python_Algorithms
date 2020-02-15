# An algorithm that finds the shortest path between two nodes of a graph with 
# the assumption that every edge has cost 1.
# Input lists: source, destination, locationA, locationB
# Example:
# source = [0, 1, 1, 1, 2, 3, 3, 4, 4, 5]
# dest = [1, 2, 3, 4, 4, 4, 5, 5, 6, 6]
# locationA = 0
# locationB = 6
#
# From source and dest the graph has:
# Nodes: 0, 1, 2, 3, 4, 5, 6
# Edges: (0, 1), (0, 2), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (3, 5), 
#        (4, 5), (4, 6), (5, 6)
#
# Result: From node 0 to node 6 the shortest hops are 3


from collections import deque

def fastestRoute(source, dest, locationA, locationB) :
    # initialize an empty queue
    queue = deque([])
    
    # initialize a set for the visited nodes
    visited = set()
    
    # initialize a list of distances. Set them initially a large numer
    dist = [float('inf')]*50
  
    # initiliaze a graph as dictionary
    graph = {}

    # generate the graph from the given source and dest lists
    for x in range(0, len(source)) :
        if source[x] in graph.keys() :
            graph[source[x]].append(dest[x])
        else :
            graph[source[x]] = [dest[x]]
      
        if dest[x] in graph.keys() :
            graph[dest[x]].append(source[x])
        else :
            graph[dest[x]] = [source[x]]
      
    Found = False
    queue.append(locationA)
    dist[locationA] = 0
  
    while queue :
        node = queue.popleft()
        visited.add(node)
        nodeDist = dist[node] 
    
        if node == locationB :
            Found = True
            break
    
        for child in graph[node] :
            childDist = nodeDist+1
      
            if childDist < dist[child] :
                dist[child] = childDist
      
            if child not in visited :
                queue.append(child)
        
    if not Found :
        return -1
    else :
        return dist[locationB]

# main program
source = [0, 1, 1, 1, 2, 3, 3, 4, 4, 5]
dest = [1, 2, 3, 4, 4, 4, 5, 5, 6, 6]
locationA = 0
locationB = 6
res = fastestRoute(source, dest, locationA, locationB)
print(res)
