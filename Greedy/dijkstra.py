from typing import List

import sys
import os
sys.path.append("../Utilities")
import math

from graph import UndirectedGraph


def dijkstra(g: UndirectedGraph, initial_node: int=0) -> List[int]:
    """
    Initialise all distances to infinity, except for initial_node which is 0.
    
    For each unseen vertex:
        - cur: vertex with minimal distance.
        - Mark cur as seen.

        - For each unseen neighbour of cur:
            - alt: cumulative distance to cur + distance to neighbour.
            - If alt < dist[neighbour]:
                - Set dist[neighbour] = alt
                - Set prev[neighbour] = cur

            # We have essentially found a better way to reach this neighbour.
            # We progressively update this until we have the best way 
            # to reach this node from our initial node.
    """


    dist = [math.inf for _ in range(g.num_vertices)]
    dist[initial_node] = 0
    prev = [None for _ in range(g.num_vertices)]
    unseen_vertices = [v for v in range(g.num_vertices)]

    while unseen_vertices:
        min_node, min_value = unseen_vertices[0], dist[0]
        for v in unseen_vertices:
            if dist[v] < min_value:
                min_node, min_value = v, dist[v]
        cur = min_node

        unseen_vertices.remove(cur)

        for neighbour in g.get_neighbours(cur):
            if neighbour in unseen_vertices:
                alt = dist[cur] + g.get_weight(cur, neighbour)
                if alt < dist[neighbour]:
                    dist[neighbour] = alt
                    prev[neighbour] = cur

    return dist, prev


if __name__ == "__main__":
    g = UndirectedGraph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    print(dijkstra(g, 3))