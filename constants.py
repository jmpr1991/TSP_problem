"""
This file contain the constants of the tsp problem
"""

import numpy as np

#  randon_vector_generator constants
n_executions = 1  #number of executions
n_cities = 100  #number of cities
dimension = 2      # space dimension
square_size = 1  # size of square in where the vectors are located
np.random.seed(2) #seed of the random function to avoid errors in the vector generator

# Initialization
n_permutations = 10 # population size (select an even number of permutations to avoid errors)

# parent selection
n_tournaments = n_permutations  # number of tournaments, lambda in the literature
gamma = 1  # number of person who win the tournament
n_individuals = 2  # number of individuals participating in the tournament

# crossover
pc = 1 # crossover probability

# mutation
pm = 1 # probability of mutation

# termination condition
n_generations = 20000 #number of generations