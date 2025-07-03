import networkx as nx
import matplotlib.pyplot as plt


# sizes = [5, 6, 6, 7, 7, 7, 8]
# s = 0.6  # Probabilidad de enlace dentro de la comunidad
# o = 0.02 # Probabilidad de enlace entre comunidades
# probs = [[s, o, o, o, o, o, o],
#         [o, s, o, o, o, o, o],
#         [o, o, s, o, o, o, o],
#         [o, o, o, s, o, o, o],
#         [o, o, o, o, s, o, o],
#         [o, o, o, o, o, s, o],
#         [o, o, o, o, o, o, s]]

# for i in range(100):
#     G = nx.stochastic_block_model(sizes, probs)
#     print(compute_network_statistics(G))


# Red con 50 nodos, cada nodo conectado a 4 vecinos, probabilidad de rewire 0.1
# G = nx.watts_strogatz_graph(n=50, k=4, p=0.1)


# Red con 25 nodos y probabilidad de enlace 0.5
# G = nx.erdos_renyi_graph(n=25, p=0.5)


# Red con 30 nodos y probabilidad de enlace 0.05
G = nx.erdos_renyi_graph(n=30, p=0.05)


nx.draw(G, with_labels=True)
plt.show()

nx.write_edgelist(G, "mygraph.edgelist", data=False)



