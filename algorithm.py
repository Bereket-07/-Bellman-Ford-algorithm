class graph:
    def __init__(self,vertics):
        self.vertics = vertics
        self.list_of_edges = []
    def add_edge(self,u,v,w):
        self.list_of_edges.append((u,v,w))
    # main method to perform the algorithm
    def bellman(self,starting_point):
        # initialize the distance from source to all other verics as infiniti
        distance = [float('inf')] * self.vertics
        distance[starting_point] = 0

        # relaxing all all edges 
        for v in range(self.vertics -1):
            for u ,v ,w in self.list_of_edges:
                if distance[u] != float('inf') and ((distance[u] + w) < distance[v]):
                    distance[v] = distance[u] + w
        # cheking for negative weight cycle 
        for u ,v ,w in self.list_of_edges:
            if distance[u] != float('inf') and ((distance[u] + w) < distance[v]):
                print("there is a negative weight cycle")
                return None
        return distance
    
    # Example usage
if __name__ == "__main__":
    # Create a graph with 5 vertices
    g = graph(5)

    # Add edges (u, v, w) where u -> v with weight w
    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)

    # Run Bellman-Ford algorithm from source vertex 0
    distances = g.bellman(0)

    if distances:
        print("Vertex Distance from Source:")
        for i, d in enumerate(distances):
            print(f"Vertex {i}: {d}")

