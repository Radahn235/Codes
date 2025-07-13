class EdgeNode:
    def __init__(self, from_vertex, to_vertex):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.next_out = None  # Next edge with the same from_vertex
        self.next_in = None   # Next edge with the same to_vertex

class Vertex:
    def __init__(self):
        self.first_out = None  # Head of list for outgoing edges
        self.first_in = None   # Head of list for incoming edges

class MultiListGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.vertices = [Vertex() for _ in range(num_vertices)]

    def add_edge(self, from_v, to_v):
        edge = EdgeNode(from_v, to_v)

        # Insert into outgoing list of from_v
        edge.next_out = self.vertices[from_v].first_out
        self.vertices[from_v].first_out = edge

        # Insert into incoming list of to_v
        edge.next_in = self.vertices[to_v].first_in
        self.vertices[to_v].first_in = edge

    def print_graph(self):
        print("Outgoing edges:")
        for i, v in enumerate(self.vertices):
            print(f"From {i}:", end=" ")
            temp = v.first_out
            while temp:
                print(f"-> {temp.to_vertex}", end=" ")
                temp = temp.next_out
            print()
        
        print("\nIncoming edges:")
        for i, v in enumerate(self.vertices):
            print(f"To {i}:", end=" ")
            temp = v.first_in
            while temp:
                print(f"<- {temp.from_vertex}", end=" ")
                temp = temp.next_in
            print()

# Example usage:
g = MultiListGraph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.print_graph()
