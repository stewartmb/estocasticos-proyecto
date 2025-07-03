no_tris = {
    'edges': 2,          # Peso para el número de enlaces
    'degree': -1,         # Peso para el grado
    'transitivity': 1,    # Peso para la transitividad
    'triangles': -2,      # Peso para el número de triángulos
    '3-stars': 1,        # Peso para el número de estrellas de 3 nodos
    '4-stars': 0.1,         # Peso para el número de estrellas de 4 nod
    '5+-stars': 0.01,          # Peso para el número de estrellas de 5 o más nodos
}

bubbles = {
    'density': 14,
    'degree': -0.4,
    'transitivity': -400, 
    'triangles': -3,
    '3-stars': -4,
    '4-stars': -4,
    '5+-stars': -4,
}


butterfly = {
    'edges': 2,
    'degree': 0,
    'transitivity': 0, 
    'triangles': -1,
    '3-stars': -3,
    '4-stars': -3,
    '5+-stars': -3,
}

star = {
    'edges': -1,
    'degree': 0,
    'transitivity': 0,   
    'triangles': 0,   
    '3-stars': -20, 
    '4-stars': 10,
}

friends = {
    'density': -500,
    'degree': 0.3,
    'degree<1': -100,
    'transitivity': 1000,
    'triangles': 0,
    # '3-stars': 0.1, 
    # '4-stars': 0.1,
    # '5+-stars': 0.01,
}

poly = {
    'density': -500,
    'degree<1': -100,
    'triangles': 0,
    '2-paths': -0.01,
    # '3-stars': 0.1, 
    # '4-stars': 0.1,
    # '5+-stars': 0.01,
}


groups = {
    'density': 1000,
    'degree<1': -0.2,
    'triangles': 0,
    '2-paths': -5,
    '3-stars': 1, 
    '4-stars': 5,
    '5+-stars': 0,
}

distant = {
    'density': -800,
    'degree': -80,
    'degree<1': -40,
    'triangles': -5,
    '2-paths': 3,
    '3-stars': -6, 
    '4-stars': -20,
    '5+-stars': -30,
}



r_params = {
    'edges': -3.2411,
    'gwesp': 0.8339,
}

g46 = {
    'edges': -3.8893,
    'gwesp': 1.0871,
    'gwd': 6.2551,
}

g50 = {
    'edges': -11.9808,
    'gwesp': 2.7129,
    'gwd': 485.3342,
    'degree<4': -10,
    'degree>4': -50,
    'transitivity': 100,
}

g25 = {
    'edges': -0.5464,
    'gwesp': 0.3483,
    'gwd': 22.4689,
}

g30 = {
    'edges': -2.4675,
    'gwesp': -0.1263,
    'gwd': 1.5929,
}