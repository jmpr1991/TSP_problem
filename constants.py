"""
This file contain the constants of the tsp problem
"""

#  randon_vector_generator constants
dimension = 2      # space dimension
square_size = 1  # size of square in where the vectors are located

# Initialization
n_permutations = 4  # number of permutations

# parent selection
n_tournaments = n_permutations  # number of tournaments, lambda in the literature
gamma = 1  # number of person who win the tournament
n_individuals = 2  # number of individuals participating in the tournament

# crossover
pc = 0.5 # crossover probability
s0 = 2 # first element of the segment used in the crossover function
sf = 4 # last element of the segment used in the crossover function