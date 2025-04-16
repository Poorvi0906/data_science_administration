class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, v, w):
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        self.adjacency_list[v].append(w)

        if w not in self.adjacency_list:
            self.adjacency_list[w] = []
        self.adjacency_list[w].append(v)

    def display(self):
        for vertex in self.adjacency_list:
            print(f"{vertex}: {self.adjacency_list[vertex]}")

# Example usage:
g = Graph()
g.add_edge('self','v')
g.add_edge('self','w')
g.add_edge('v','none')
g.display()



