import networkx as nx
import matplotlib.pyplot as plt
import random
from estadisticas import calcular
import math
import copy
from params import *


n = 16           # Número de nodos en el grafo
p = 0.05          # Probabilidad inicial de conexión
iteraciones = 5000  # Número de modificaciones aleatorias

params = no_tris # Parámetros iniciales

def change(G_propuesto):
    # Proponer un cambio: añadir o quitar una arista
        i, j = random.sample(range(G.number_of_nodes()), 2)
        if G_propuesto.has_edge(i, j):
            G_propuesto.remove_edge(i, j)
        else:
            G_propuesto.add_edge(i, j)

def mcmc_grafo(G, calcular, params, iteraciones=10000):
    puntaje_actual = calcular(G, params)

    for i in range(iteraciones):
        # Crear una copia del grafo actual
        G_propuesto = copy.deepcopy(G)

        for _ in range(random.randint(1, 3)):  # Realizar entre 1 y 3 cambios aleatorios
            change(G_propuesto)

        # Calcular el puntaje del grafo propuesto
        show = (i% 100 == 0)
        puntaje_nuevo = calcular(G_propuesto, params, debug=show)

        # Diferencia de puntajes
        delta = puntaje_nuevo - puntaje_actual

        # Regla de aceptación (tipo Metropolis-Hastings)
        if delta >= 0:
            G = G_propuesto
            puntaje_actual = puntaje_nuevo
        else:
            if random.random() < math.exp(delta):
                G = G_propuesto
                puntaje_actual = puntaje_nuevo

    return G


# Crear grafo aleatorio inicial (no dirigido)
G = nx.erdos_renyi_graph(n=n, p=p)

G = mcmc_grafo(G, calcular, params, iteraciones=iteraciones)

print(calcular(G, params))

# Dibujar el grafo final
plt.figure(figsize=(10, 8))
nx.draw(
    G,
    with_labels=True,
    node_color='lightblue',
    node_size=300,
    edge_color='black',
    font_weight='bold'
)
plt.title(f"Grafo después de {iteraciones} cambios aleatorios", fontsize=16)
plt.show()
