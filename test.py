import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph (MultiDiGraph allows multiple edges between nodes)
G = nx.MultiDiGraph()

# Define states
states = {"A": "Even Position", "B": "Odd Position"}

# Add nodes
for state, label in states.items():
    G.add_node(state, label=label)

# Add edges with input/output labels
edges = [
    ("A", "B", "0/0"),
    ("A", "B", "1/1"),
    ("B", "A", "0/1"),
    ("B", "A", "1/0"),
]

for u, v, label in edges:
    G.add_edge(u, v, label=label)

# Define layout
pos = nx.spring_layout(G, seed=42)  # Fixed layout for consistency

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2000,
    node_color="lightblue",
    font_size=12,
    font_weight="bold",
    edgecolors="black",
)

# Draw node labels separately
node_labels = {node: states[node] for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10)

# Draw edge labels
edge_labels = {(u, v): d["label"] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red")

plt.title("State Diagram of the FST")
plt.show()
