# -*- coding: utf-8 -*-
"""
Tarea 8. Kruskal
"""
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import tree
# Crea un grafo no dirigio
G = nx.Graph()
# Agregamos los vetices al grafo
G.add_nodes_from(range(10))
#Generamos cada una de las aristas con sus pesos
G.add_edge(0, 1, weight=2)#1
G.add_edge(0, 2, weight=4)#2
G.add_edge(0, 3, weight=1)#3
G.add_edge(0, 4, weight=8)#4
G.add_edge(1, 2, weight=3)#5
G.add_edge(1, 3, weight=2)#6
G.add_edge(1, 4, weight=7)#7
G.add_edge(2, 5, weight=15)#8    
G.add_edge(2, 4, weight=7)#9
G.add_edge(3, 4, weight=8)#10
G.add_edge(3, 5, weight=1)#11
G.add_edge(3, 6, weight=21)#12
G.add_edge(7, 9, weight=13)#13
G.add_edge(4, 5, weight=14)#14
G.add_edge(4, 6, weight=5)#15
G.add_edge(4, 7, weight=6)#16
G.add_edge(5, 1, weight=9)#17
G.add_edge(5, 7, weight=12)#18
G.add_edge(6, 7, weight=24)#19
G.add_edge(6, 8, weight=11)#20
G.add_edge(6, 9, weight=19)#21
G.add_edge(7, 8, weight=10)#22
G.add_edge(9, 2, weight=18)#23
G.add_edge(8, 9, weight=16)#24
G.add_edge(8, 0, weight=16)#25
#Definimos la posicion de los nodos 
pos = {
    0: (0, 1), 1: (1, 0.6), 2: (2, 1), 3: (0, 0), 4: (1, 0), 
    5: (2, 0), 6: (0.3, 0.5), 7: (1.7, 0.5), 8: (0.5, 1.5), 9: (1.5, 1.5)
}
#Dibujamos el grafo ponderado
plt.figure(figsize=(6, 6))
plt.suptitle("Grafo ponderado")
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
#Calculamos el kruskal y lo dibujamos
plt.figure(figsize=(6, 6))
plt.suptitle("Kruskal")
mst = tree.minimum_spanning_edges(G, algorithm='kruskal', data=False)
edgelist = list(mst)#Lista de aristas del mst
nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=500)
nx.draw_networkx_edges(G, pos, edgelist=edgelist, width=6, alpha=0.5, edge_color='g')
#Mostramos el grafo
plt.show()
