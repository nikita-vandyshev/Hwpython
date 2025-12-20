class Graph:
    def __init__(self):
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, a, b):
        self.add_vertex(a)
        self.add_vertex(b)
        self.adj[a].append(b)
        self.adj[b].append(a)

    def dfs(self, start):
        visited = set()
        order = []

        def go(v):
            visited.add(v)
            order.append(v)

            for to in self.adj.get(v, []):
                if to not in visited:
                    go(to)

        go(start)
        return order

    def __iter__(self):
        visited = set()

        def dfs_from(start):
            stack = [start]
            while stack:
                v = stack.pop()
                if v in visited:
                    continue
                visited.add(v)
                yield v

                neigh = self.adj.get(v, [])
                for to in reversed(neigh):
                    if to not in visited:
                        stack.append(to)

        for v in self.adj:
            if v not in visited:
                yield from dfs_from(v)


if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 5)

    print("DFS from 1:", g.dfs(1))

    print("Iterate graph in DFS order:")
    for v in g:
        print(v)
