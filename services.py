class graph:
    def __init__(self,vertics):
        self.vertics = vertics
        self.list_of_edges = []
    def add_edge(self,u,v,w):
        self.list_of_edges.append((u,v,w))
    # main method to perform the algorithm
    def bellman(self, start, end, max_stops):
        # initialize the distance from source to all other verics as infiniti
        distance = [float('inf')] * self.vertics
        distance[start] = 0
        paths = [[] for _ in range(self.vertics)]
        paths[start] = [start]

        # Relax edges up to max_stops + 1 times
        for _ in range(max_stops + 1):
            temp_distances = distance[:]
            temp_paths = [path[:] for path in paths]

            for u, v, w in self.list_of_edges:
                if distance[u] != float('inf') and (temp_distances[v] > distance[u] + w):
                    temp_distances[v] = distance[u] + w
                    temp_paths[v] = paths[u] + [v]

            distance = temp_distances
            paths = temp_paths

        if distance[end] == float('inf'):
            print("No path found within the maximum number of stops.")
            return None, []

        return distance[end], paths[end]
    
#  # Example usage
# if __name__ == "__main__":
#     N = 4
#     g = graph(N)

#     # Add edges (u, v, w)
#     g.add_edge(0, 1, 100)
#     g.add_edge(1, 2, 100)
#     g.add_edge(0, 2, 500)

#     # Set parameters
#     START = 0
#     END = 2
#     MAX_STOPS = 1

#     # Find shortest path
#     distance, path = g.bellman(START, END, MAX_STOPS)

#     if distance is not None:
#         print("Distance:", distance)
#         print("Path:", " -> ".join(map(str, path)))

