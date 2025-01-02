import networkx as nx
import matplotlib.pyplot as plt
from difflib import get_close_matches
from graph import cities, connections

# Create a graph object
G = nx.Graph()

# Add nodes (cities) to the graph
G.add_nodes_from(cities)

# Add edges with weights
for city1, city2, distance in connections:
    G.add_edge(city1, city2, weight=distance)


# Function to plot the graph with the shortest path highlighted
def plot_shortest_path(G, start, end, algorithm="dijkstra"):
    try:
        if algorithm == "dijkstra":
            shortest_path = nx.dijkstra_path(G, start, end, weight="weight")
        elif algorithm == "bellman-ford":
            shortest_path = nx.bellman_ford_path(G, start, end, weight="weight")
        else:
            print("Invalid algorithm selected!")
            return

        shortest_path_edges = list(zip(shortest_path, shortest_path[1:]))

        # Get edge weights for visualization
        edge_labels = nx.get_edge_attributes(G, "weight")

        # Draw the graph
        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(G, seed=42)  # Layout for better visualization
        nx.draw(
            G,
            pos,
            with_labels=True,
            node_color="lightblue",
            edge_color="gray",
            font_size=8,
            font_weight="bold",
        )
        # Highlight the shortest path
        nx.draw_networkx_edges(
            G, pos, edgelist=shortest_path_edges, edge_color="red", width=2
        )
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

        # Add a title
        plt.title(
            f"Shortest Path from {start} to {end} ({algorithm.capitalize()} Algorithm)",
            fontsize=16,
        )
        plt.show()
    except nx.NetworkXNoPath:
        print(f"No path exists between {start} and {end}.")
    except nx.NodeNotFound as e:
        print(f"Error: {e}")


# Suggest closest matches for invalid city names
def suggest_city(input_city, cities):
    matches = get_close_matches(input_city, cities)
    if matches:
        print(f"Did you mean: {', '.join(matches)}?")
    else:
        print("No similar city names found.")


# Function to plot the graph with paths from both algorithms side by side
def plot_all_algorithms(G, start, end):
    try:
        # Compute shortest paths for both algorithms
        dijkstra_path = nx.dijkstra_path(G, start, end, weight="weight")
        bellman_ford_path = nx.bellman_ford_path(G, start, end, weight="weight")

        dijkstra_edges = list(zip(dijkstra_path, dijkstra_path[1:]))
        bellman_ford_edges = list(zip(bellman_ford_path, bellman_ford_path[1:]))

        # Get edge weights for visualization
        edge_labels = nx.get_edge_attributes(G, "weight")

        # Plot the graph
        plt.figure(figsize=(16, 8))
        pos = nx.spring_layout(G, seed=42)  # Layout for better visualization

        # Plot Dijkstra's Algorithm
        plt.subplot(1, 2, 1)
        nx.draw(
            G,
            pos,
            with_labels=True,
            node_color="lightblue",
            edge_color="gray",
            font_size=8,
            font_weight="bold",
        )
        nx.draw_networkx_edges(
            G, pos, edgelist=dijkstra_edges, edge_color="red", width=2
        )
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
        plt.title("Shortest Path (Dijkstra's Algorithm)", fontsize=14)

        # Plot Bellman-Ford Algorithm
        plt.subplot(1, 2, 2)
        nx.draw(
            G,
            pos,
            with_labels=True,
            node_color="lightblue",
            edge_color="gray",
            font_size=8,
            font_weight="bold",
        )
        nx.draw_networkx_edges(
            G, pos, edgelist=bellman_ford_edges, edge_color="green", width=2
        )
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
        plt.title("Shortest Path (Bellman-Ford Algorithm)", fontsize=14)

        plt.tight_layout()
        plt.show()

    except nx.NetworkXNoPath:
        print(f"No path exists between {start} and {end}.")
    except nx.NodeNotFound as e:
        print(f"Error: {e}")


# Update menu-driven interface
def main():
    while True:
        print("\n--- Graph Shortest Path Finder ---")
        print("1. Find shortest path (single algorithm)")
        print("2. Compare all algorithms")
        print("3. View graph")
        print("4. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            print("\nAvailable cities:")
            print(", ".join(cities))
            start_city = input("Enter the start city: ").strip()
            end_city = input("Enter the end city: ").strip()

            if start_city not in cities:
                print(f"{start_city} not found!")
                suggest_city(start_city, cities)
                continue
            if end_city not in cities:
                print(f"{end_city} not found!")
                suggest_city(end_city, cities)
                continue

            print("\nChoose algorithm:")
            print("1. Dijkstra")
            print("2. Bellman-Ford")
            algo_choice = input("Enter your choice: ").strip()

            if algo_choice == "1":
                plot_shortest_path(G, start_city, end_city, algorithm="dijkstra")
            elif algo_choice == "2":
                plot_shortest_path(G, start_city, end_city, algorithm="bellman-ford")
            else:
                print("Invalid algorithm choice!")

        elif choice == "2":
            print("\nAvailable cities:")
            print(", ".join(cities))
            start_city = input("Enter the start city: ").strip()
            end_city = input("Enter the end city: ").strip()

            if start_city not in cities:
                print(f"{start_city} not found!")
                suggest_city(start_city, cities)
                continue
            if end_city not in cities:
                print(f"{end_city} not found!")
                suggest_city(end_city, cities)
                continue

            plot_all_algorithms(G, start_city, end_city)

        elif choice == "3":
            # Visualize the graph
            plt.figure(figsize=(12, 8))
            pos = nx.spring_layout(G, seed=42)
            edge_labels = nx.get_edge_attributes(G, "weight")
            nx.draw(
                G,
                pos,
                with_labels=True,
                node_color="lightblue",
                edge_color="gray",
                font_size=8,
                font_weight="bold",
            )
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
            plt.title("Graph Visualization", fontsize=16)
            plt.show()

        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


# Run the program
if __name__ == "__main__":
    main()
