from collections import defaultdict
import heapq
import math
from copy import deepcopy
from typing import List

class Graph():
    def __init__(self, connections=None, weighted=False):
        # if it's not a weighted graph, initialize all the weights to be 1
        
        self.weighted = weighted

        if connections:
            self._graph = connections 
        else:
            self._graph = defaultdict(dict)


    # add the __attr__?
    def __repr__(self):
        # if not self.weighted, omit weights
        res = ""
        if self.weighted:
            for key in self._graph:
                res += f"{key} -> {self._graph[key]}\n"
        else: 
            for key in self._graph:
                res += f"{key} -> {list(self._graph[key].keys())}\n"

        return res

    def __getitem__(self, vertex):
        return self._graph[vertex]

    
    def add_edge(self, u: str, vs: List[str], weights: List[float] = None):
        """given a key u, append another node v to it with weight 1 unless otherwise specified"""

        # TODO add exceptions for diff shaped lists
        if self.weighted:
            if not weights or len(weights) != len(vs):
                print("invalid arguments")
                raise Exception
            for v, w in zip(vs, weights):
                self._graph[u][v] = w 
        else:
            for v in vs:
                self._graph[u][v] = 1 

            

    def degree(self, vertex):
        """Given a vertex (key within _graph), return the number of adjacent vertices"""
        return len(self._graph[vertex]) 

    def breadth_first(self, s):
        """performs a BFS from vertex s to t"""
        visited = defaultdict(bool)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)
            print (u, end = " ")

            for v in self._graph[u].keys():
                if not visited[v]:
                    queue.append(v)
                    visited[v] = True
        print()


    def breadth_first_search(self, s, t):
        """searches for t starting from s"""
        visited = []
        path_queue = [[s]]
        
        if s == t:
            return [s]
        
        while path_queue:
            path = path_queue.pop(0)
            current = path[-1]
            if current not in visited:
                neighbors = list(self._graph[current].keys())
                for n in neighbors:
                    new_path = list(path)
                    new_path.append(n)
                    path_queue.append(new_path)
                    if n == t:
                        return new_path
                
                visited.append(n)
        
        return []

    def dijkstras(self, start):
        # Q = {v: float('infinity') for v in self._graph.keys()}
        Q = defaultdict(lambda: float("infinity"))
        Q[start] = 0.0

        pq = [(0, start)]
        while pq:
            dist, v = heapq.heappop(pq)
            
            if dist > Q[v]:
                continue
            
            for neighbor, weight in self._graph[v].items():
                dist_prime = dist + weight 

                if dist_prime < Q[neighbor]:
                    Q[neighbor] = dist_prime
                    heapq.heappush(pq, (dist_prime, neighbor))
        return dict(Q)


    # TODO this isn't totally right
    def operation_save_will_beyers(self, target, r):
        connections = defaultdict(dict)

        for u, neighbors in self._graph.items():
            for v, w in neighbors.items():
                connections[u][v] = -math.log(w)
        
        # print(dict(connections))
        
        g = Graph(connections=connections, weighted=True)
        print(g)

        path = g.dijkstras("a")
        for v, cost in path.items():
            if cost < -math.log(r):
                return True

        return False 




if __name__ == "__main__":
    # g = Graph()
    # g.add_edge("a", ["b", "c"])
    # g.add_edge("b", ["e", "d", "f"])
    # g.add_edge("f", ["g"])
    # print(g)
    # print(g.dijkstras("a"))


    # weighted_g = Graph(weighted=True)
    # weighted_g.add_edge("a", ["b", "c"], weights=[0.1, 1])
    # weighted_g.add_edge("b", ["e", "d", "f"], weights=[0.1, 0.5, 1])
    # print(weighted_g)

    # # weighted_g.breadth_first("a")
    # print(weighted_g.breadth_first_search("a", "f"))
    # print(weighted_g.dijkstras("a"))

    upside_down = Graph(weighted=True)
    upside_down.add_edge("a", ["b", "c", "g"], weights=[1.0, 0.5, 0.02])
    upside_down.add_edge("b", ["c"], weights=[0.8])
    upside_down.add_edge("c", ["d"], weights=[0.6])
    upside_down.add_edge("e", ["d", "f"], weights=[0.5, 0.5])
    upside_down.add_edge("f", ["g"], weights=[0.5])
    upside_down.add_edge("d", ["g"], weights=[0.7])
    print(upside_down)

    print(upside_down.operation_save_will_beyers("g", 2.0))
    
    


