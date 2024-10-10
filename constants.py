"""
This file contain the constants of the tsp problem
"""

#  randon_vector_generator constants
dimension = 2      # space dimension
square_size = 1  # size of square in where the vectors are located

# Initialization constants
n_permutations = 4  # number of permutations

# father selection
n_tournaments = n_permutations  # number of tournaments, lambda in the literature
gamma = 1  # number of person who win the tournament
n_individuals = 2  # number of individuals participating in the tournament
