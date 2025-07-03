import networkx as nx
import matplotlib.pyplot as plt
from estadisticas import calcular, compute_network_statistics

G = nx.read_edgelist("g25.edgelist")

# Calcular estadísticas de la red
stats = compute_network_statistics(G)
print(stats)

# 2. Dibujar el grafo
plt.figure(figsize=(8, 6))
nx.draw(
    G,
    with_labels=True,
    node_color='lightblue',
    node_size=300,
    edge_color='black',
    font_weight='bold'
)
plt.title("Grafo cargado desde una edgelist", fontsize=14)
plt.show()
