import networkx as nx
import matplotlib.pyplot as plt
from estadisticas import calcular, compute_network_statistics

# Dos comunidades de 30 y 40 nodos
sizes = [5, 6, 6, 7, 7, 7, 8]
s = 0.6  # Probabilidad de enlace dentro de la comunidad
o = 0.02 # Probabilidad de enlace entre comunidades
probs = [[s, o, o, o, o, o, o],
        [o, s, o, o, o, o, o],
        [o, o, s, o, o, o, o],
        [o, o, o, s, o, o, o],
        [o, o, o, o, s, o, o],
        [o, o, o, o, o, s, o],
        [o, o, o, o, o, o, s]]

for i in range(100):
    G = nx.stochastic_block_model(sizes, probs)
    print(compute_network_statistics(G))

nx.write_edgelist(G, "mygraph.edgelist", data=False)
nx.draw(G, with_labels=True)
plt.show()

