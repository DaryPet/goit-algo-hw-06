import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import heapq

# Make empty graph
G = nx.Graph()

# add people (nodes)
G.add_nodes_from(["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"])

# add edges (relations)
# G.add_edges_from(
#     [
#     ("Alice", "Bob", weight=1),
#     ("Alice", "Charlie"),
#     ("Bob", "David"),
#     ("Charlie", "Eve"),
#     ("David", "Eve"),
#     ("Eve", "Frank"),
#     ("Frank", "Grace"),
#     ("Grace", "Alice")
#     ]
# )
G.add_edge("Alice", "Bob", weight=1)
G.add_edge("Alice", "Charlie", weight=4)
G.add_edge("Bob", "David", weight=2)
G.add_edge("Charlie", "Eve", weight=5)
G.add_edge("David", "Eve", weight=1)
G.add_edge("Eve", "Frank", weight=3)
G.add_edge("Frank", "Grace", weight=2)
G.add_edge("Grace", "Alice", weight=8)
# ======================================================================
# TASK - 2
# DFS
def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path =[]
    if visited is None:
        visited = set()

    path.append(start)
    visited.add(start)

    if start == goal:
        return path
    
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, path, visited)
            if result:
                return result
    path.pop()
    return None

# BFS
def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        (vertex, path) = queue.popleft()
        for neighbor in graph.neighbors(vertex):
            if neighbor not in visited:
                if neighbor == goal:
                    return path + [neighbor]
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

# ======================================================================================
# TASK - 3

def dijkstra(graph, start):
    shortest_path = nx.single_source_dijkstra_path(graph, source=start)
    shortes_path_lengths = nx.single_source_dijkstra_path_length(graph, source=start)
  
    return shortest_path, shortes_path_lengths

# Print numbers of nodes and edges
print(f"Nubmers of nodes(people): {G.number_of_nodes}")
print(f"Number of edges (relations): {G.number_of_edges}")
# how many friends each peopson has
print ("Numbers of friends:")
for node in G.nodes():
    print(f"{node}: {G.degree(node)}")

# testing DFS
dfs_path = dfs(G, "Alice", "Frank")
print("DFS - Path from Alice to Frank:", dfs_path)
# testing BFS
bfs_path = bfs(G, "Alice", "Frank")
print("BFS - Path from Alice to Frank:", bfs_path)
# DK
shortest_path, shortest_path_lengths = dijkstra(G, "Alice")
print("The shortest way from Alice to others:" )
for node, path in shortest_path.items():
    print(f"Alice => {node}: {path}")
print(f"Shortest way from Alice to all other's nodes:")
for node, distance in shortest_path_lengths.items():
    print(f"Alice => {node}: {distance}")

# Visualization
plt.figure(figsize=(8,6))

pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("Social network")
plt.show()