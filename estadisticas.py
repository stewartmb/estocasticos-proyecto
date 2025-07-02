import networkx as nx
import math

def alt_2_path_open_undirected(G):
    """
    Cuenta el número de 2-paths abiertos en grafo no dirigido G,
    es decir, triples (i,j,k) con i-j, j-k, y no i-k.
    """
    count = 0
    for j in G.nodes():
        neighbors = list(G.neighbors(j))
        # Chequeamos todos pares (i,k) vecinos de j
        for idx_i in range(len(neighbors)):
            for idx_k in range(idx_i + 1, len(neighbors)):
                i = neighbors[idx_i]
                k = neighbors[idx_k]
                # Cuenta solo si NO hay enlace i-k
                if not G.has_edge(i, k):
                    count += 1
    return count


def calcular_estadisticas_de_red(G):
    stats = {}

    # 1. Número de enlaces (aristas)
    stats['edges'] = G.number_of_edges()

    stats['density'] = nx.density(G)

    # 2. Grado promedio
    grados = [grado for nodo, grado in G.degree()]
    stats['degree'] = sum(grados) / len(grados) if grados else 0

    stats['degree<1'] = sum(1 for g in grados if g <= 1)

    # 3. Transitividad (clustering global)
    stats['transitivity'] = nx.transitivity(G)

    # 4. K-Triángulos (triángulos por nodo, total dividido por 3 para evitar contar 3 veces)
    tri_por_nodo = nx.triangles(G)
    stats['triangles'] = sum(tri_por_nodo.values()) // 3

    k_estrella_count = sum(1 for g in grados if g == 3)
    stats['3-stars'] = k_estrella_count

    k_estrella_count = sum(1 for g in grados if g == 4)
    stats['4-stars'] = k_estrella_count

    k_estrella_count = sum(1 for g in grados if g >= 5)
    stats['5+-stars'] = k_estrella_count

    stats['offset'] = 1

    stats['2-paths'] = alt_2_path_open_undirected(G)

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