import numpy as np

def initialize_population(pop_size, n_genes, pop_type):
    if pop_type not in ["binary", "continuous"]:
        raise AssertionError("Population type must be 'Binary' or 'Continuous'")
	
    if pop_type == "binary":
        population = np.random.randint(0, 2, size=(pop_size, n_genes))
    elif pop_type == "continuous": 
        population = np.random.uniform(size=(pop_size, n_genes))

    return population
