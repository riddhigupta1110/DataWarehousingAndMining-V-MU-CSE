import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph interactively
num_edges = int(input("Enter the number of edges: "))
for _ in range(num_edges):
    source, target = input("Enter edge (Source, Target): ").split()
    G.add_edge(source, target)

# Get the damping factor from the user
damping_factor = float(input("Enter the Damping Factor: "))

# Calculate PageRank using NetworkX's built-in function
pagerank_scores = nx.pagerank(G, alpha=damping_factor)
nx.draw(G, with_labels=True, arrows=True)
plt.show()

# Display PageRank scores
print("PageRank Scores:")
for node, score in pagerank_scores.items():
    print(f"Node {node}: {score:.4f}")
