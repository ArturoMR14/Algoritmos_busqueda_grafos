import matplotlib.pyplot as plt
import networkx as nx

def buscar(padre, i):
    if padre[i] == i:
        return i
    return buscar(padre, padre[i])

def unir(padre, rango, x, y):
    raiz_x = buscar(padre, x)
    raiz_y = buscar(padre, y)

    if rango[raiz_x] < rango[raiz_y]:
        padre[raiz_x] = raiz_y
    elif rango[raiz_x] > rango[raiz_y]:
        padre[raiz_y] = raiz_x
    else:
        padre[raiz_y] = raiz_x
        rango[raiz_x] += 1

def kruskal(vertices, aristas):
    resultado = []
    aristas = sorted(aristas, key=lambda item: item[2])
    padre = list(range(vertices))
    rango = [0] * vertices
    e = 0
    i = 0

    while e < vertices - 1:
        u, v, w = aristas[i]
        i += 1
        x = buscar(padre, u)
        y = buscar(padre, v)

        if x != y:
            e += 1
            resultado.append([u, v, w])
            unir(padre, rango, x, y)

    return resultado


#Ejemplo de uso
V = 7  # Número de vértices
aristas = [
    [0, 1, 7],
    [0, 3, 5],
    [1, 2, 8],
    [1, 3, 9],
    [1, 4, 7],
    [2, 4, 5],
    [3, 4, 15],
    [3, 5, 6],
    [4, 5, 8],
    [4, 6, 9],
    [5, 6, 11]
]

#Crear el grafo original
G = nx.Graph()
G.add_nodes_from(range(V))
G.add_weighted_edges_from(aristas)

#Obtener el árbol de expansión mínimo
arbol_expansion = kruskal(V, aristas)

#Crear el grafo del árbol de expansión mínimo
T = nx.Graph()
T.add_nodes_from(range(V))
T.add_weighted_edges_from(arbol_expansion)

#Mostrar los grafos
plt.figure(figsize=(10, 4))

#Grafo original
plt.subplot(121)
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, node_color='lightblue', node_size=500, edgecolors='black')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Grafo original")

#Arbol de expansión mínimo
plt.subplot(122)
pos = nx.spring_layout(T)
nx.draw_networkx(T, pos, node_color='lightgreen', node_size=500, edgecolors='black')
labels = nx.get_edge_attributes(T, 'weight')
nx.draw_networkx_edge_labels(T, pos, edge_labels=labels)
plt.title("Arbol de expansión minimo")

plt.tight_layout()
plt.show()
