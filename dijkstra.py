import sys
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start, end):
    
    # Inicialización de distancias y nodos visitados
    distances = {node: sys.maxsize for node in graph}
    distances[start] = 0
    visited = set()

    while len(visited) < len(graph):
        # Encuentra el nodo con la distancia mínima no visitado
        min_distance = sys.maxsize
        min_node = None

        for node in graph:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node

        visited.add(min_node)

        # Si se alcanza el nodo destino, se detiene el algoritmo
        if min_node == end:
            break

        # Actualiza las distancias de los nodos vecinos no visitados
        for neighbor, weight in graph[min_node].items():
            if neighbor not in visited:
                new_distance = distances[min_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

        # Visualización gráfica de la iteración actual
        visualize_graph(graph, distances, visited, start, end)

    return distances

def visualize_graph(graph, distances, visited, start, end):
    G = nx.DiGraph()
    labels = {}
    node_colors = []

    for node, neighbors in graph.items():
        G.add_node(node)
        labels[node] = node

        if node == start:
            node_colors.append('blue')
        elif node == end:
            node_colors.append('red')
        elif node in visited:
            node_colors.append('lightgreen')
        else:
            node_colors.append('lightblue')

        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')

    plt.clf()
    nx.draw(G, pos, with_labels=True, node_color=node_colors)
    nx.draw_networkx_labels(G, pos, labels=labels)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title(" Algoritmo Dijkstra")
    plt.show(block=False)
    plt.pause(1)

# Ejemplo de grafo de prueba
graph = {
    'A': {'B': 2, 'C': 3, 'D': 5},
    'B': {'A': 2, 'C': 4, 'E': 1},
    'C': {'A': 3, 'B': 4, 'D': 2, 'E': 4, 'F': 3},
    'D': {'A': 5, 'C': 2, 'F': 1, 'G': 4},
    'E': {'B': 1, 'C': 4, 'F': 2, 'H': 3},
    'F': {'C': 3, 'D': 1, 'E': 2, 'G': 2, 'H': 4},
    'G': {'D': 4, 'F': 2, 'I': 3},
    'H': {'E': 3, 'F': 4, 'I': 1},
    'I': {'G': 3, 'H': 1, 'J': 5},
    'J': {'I': 5}
}

start_node = 'A'
end_node = 'J'
distances = dijkstra(graph, start_node, end_node)

print("Distancias mínimas desde el nodo de origen (", start_node, "):")
for node, distance in distances.items():
    print("Nodo:", node, "Distancia:", distance)

# Reconstruye el camino más corto
path = [end_node]
current_node = end_node
while current_node != start_node:
    for neighbor, weight in graph[current_node].items():
        if distances[current_node] == distances[neighbor] + weight:
            path.append(neighbor)
            current_node = neighbor
            break
path.reverse()
#Imprime el resultado de la busqueda 
print("Camino más corto desde", start_node, "hasta", end_node, ":")
print(" -> ".join(path))
