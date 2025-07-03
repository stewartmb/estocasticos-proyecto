import networkx as nx
import numpy as np
import math


def gwesp_statistic(G, tau=0.25):
    e_tau = np.exp(tau)
    factor = 1 - np.exp(-tau)
    max_i = len(G.nodes) - 2

    # Contador para EP_i
    ep_counts = {}

    for (u, v) in G.edges():
        # Vecinos comunes de u y v
        common_neighbors = list(nx.common_neighbors(G, u, v))
        i = len(common_neighbors)

        if i > 0:
            ep_counts[i] = ep_counts.get(i, 0) + 1

    # Calcular la suma ponderada
    stat_sum = 0.0
    for i, count in ep_counts.items():
        weight = 1 - (1 - factor) ** i
        stat_sum += weight * count

    v_x_tau = e_tau * stat_sum
    return v_x_tau


def gwd_statistic(G, tau=0.25):
    e_tau = np.exp(tau)
    factor = 1 - np.exp(-tau)

    # Contar número de nodos con cada grado
    degrees = dict(G.degree())
    degree_counts = {}

    for deg in degrees.values():
        if deg > 0:
            degree_counts[deg] = degree_counts.get(deg, 0) + 1

    stat_sum = 0.0
    for i, count in degree_counts.items():
        weight = 1 - (1 - factor) ** i
        stat_sum += weight * count

    u_x_tau = e_tau * stat_sum
    return u_x_tau


def calcular_estadisticas_de_red(G):
    stats = {}

    # 1. Número de enlaces (aristas)
    stats['edges'] = G.number_of_edges()

    stats['gwesp'] = gwesp_statistic(G)
    stats['gwd'] = gwd_statistic(G)

    grados = [grado for nodo, grado in G.degree()]

    stats['degree<4'] = sum((4-g) for g in grados if g < 4)
    stats['degree>4'] = sum((g-4) for g in grados if g > 4)

    stats['transitivity'] = nx.transitivity(G)

    return stats


def calcular(G, params, debug=False):
    stats = calcular_estadisticas_de_red(G)
    if debug:
        print(stats)
    result = 0
    for key in params:
        if key in stats:
            result += stats[key] * params[key]
        else:
            print(f"Warning: '{key}' not found in statistics.")
    if debug:
        print(f"Result: {result}")
    return result


def compute_network_statistics(G):
    """
    Recibe un grafo networkx G y devuelve un vector (lista) con:
    [NLC, L, avg_degree, avg_clustering, assortativity, avg_path_length, diameter]
    """
    # Extraer mayor componente conexa
    largest_cc = max(nx.connected_components(G), key=len)
    G_sub = G.subgraph(largest_cc).copy()
    
    # NLC: número de nodos en la mayor componente conexa
    NLC = len(largest_cc)
    
    # L: número de aristas
    L = G.number_of_edges()
    
    # Grado promedio
    avg_degree = sum(dict(G.degree()).values()) / G.number_of_nodes()
    
    # Clustering promedio
    avg_clustering = nx.average_clustering(G)
    
    # Coeficiente de assortativity
    try:
        assortativity = nx.degree_pearson_correlation_coefficient(G)
    except:
        assortativity = float('nan')  # Si no se puede calcular
    
    # Longitud de camino promedio (solo en componente conexa)
    try:
        avg_path_length = nx.average_shortest_path_length(G_sub)
    except:
        avg_path_length = float('nan')
    
    # Diámetro (solo en componente conexa)
    try:
        diameter = nx.diameter(G_sub)
    except:
        diameter = float('nan')
    
    # Devolver como vector (lista)
    stats_vector = [NLC, L, avg_degree, avg_clustering, assortativity, avg_path_length, diameter]
    
    return stats_vector