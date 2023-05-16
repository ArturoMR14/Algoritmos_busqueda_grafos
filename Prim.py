import sys
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
    
    def printMST(self, parent):
        G = nx.Graph()
        for i in range(1, self.V):
            G.add_edge(parent[i], i, weight=self.graph[i][parent[i]])
        
        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_nodes(G, pos, node_size=700)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.title("Arbol de expansión minima")
        plt.show(block=False)
        plt.pause(2)
        plt.clf()
        plt.pause(.5)
    
    def minKey(self, key, mstSet):
        min_val = sys.maxsize
        min_index = -1
        
        for v in range(self.V):
            if key[v] < min_val and not mstSet[v]:
                min_val = key[v]
                min_index = v
        
        return min_index
    
    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        
        parent[0] = -1
        
        for _ in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            
            for v in range(self.V):
                if (
                    self.graph[u][v] > 0 and
                    not mstSet[v] and
                    self.graph[u][v] < key[v]
                ):
                    key[v] = self.graph[u][v]
                    parent[v] = u
        
        self.printMST(parent)

# Ejemplo de uso del algoritmo de Prim

g = Graph(8)
g.graph = [
    [0, 2, 0, 6, 0, 0, 0, 0],
    [2, 0, 3, 8, 5, 0, 0, 0],
    [0, 3, 0, 0, 7, 0, 0, 0],
    [6, 8, 0, 0, 9, 0, 0, 0],
    [0, 5, 7, 9, 0, 4, 2, 0],
    [0, 0, 0, 0, 4, 0, 0, 3],
    [0, 0, 0, 0, 2, 0, 0, 1],
    [0, 0, 0, 0, 0, 3, 1, 0]
]

G = nx.Graph()
for i in range(g.V):
    G.add_node(i)
for i in range(g.V):
    for j in range(i + 1, g.V):
        if g.graph[i][j] != 0:
            G.add_edge(i, j, weight=g.graph[i][j])

pos = nx.spring_layout(G)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Grafo original")
plt.show(block=False)
plt.pause(2)
plt.clf()

g.primMST()
