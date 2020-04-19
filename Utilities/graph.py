class Graph:
    def __init__(self, num_vertices: int):
        self._edges = [[0 for _ in range(num_vertices)]
                       for _ in range(num_vertices)]

    def is_adjacent(self, v: int, w: int) -> bool:
        return self._edges[v][w] != 0
    
    def add_edge(self, v: int, w: int, weight: int=1) -> None:
        self._edges[v][w] = weight

    def remove_edge(self, v: int, w: int) -> None:
        self._edges[v][w] = 0


class UndirectedGraph(Graph):
    def add_edge(self, v: int, w: int, weight: int=1) -> None:
        self._edges[v][w] = weight
        self._edges[w][v] = weight

    def remove_edge(self, v: int, w: int) -> None:
        self._edges[v][w] = 0
        self._edges[w][v] = 0