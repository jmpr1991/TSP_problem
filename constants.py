"""
This file contain the constants of the tsp problem
"""

import numpy as np

#  randon_vector_generator constants
n_executions = 2
n_cities = 100
dimension = 2      # space dimension
square_size = 1  # size of square in where the vectors are located
np.random.seed(2) #seed of the random function to avoid errors in the vector generator

# Initialization
n_permutations = 6 # number of permutations (select an even number of permutations to avoid errors)

# parent selection
n_tournaments = n_permutations  # number of tournaments, lambda in the literature
gamma = 1  # number of person who win the tournament
n_individuals = 2  # number of individuals participating in the tournament

# crossover
pc = 0.5 # crossover probability

# mutation
pm = 0.5 # probability of mutation

# termination condition
n_generations = 1000 #number of generations