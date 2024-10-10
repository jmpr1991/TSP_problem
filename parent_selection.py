import constants
import evaluation

import numpy as np


def parent_selection_function(individuals_vector, distance_vector, n_cities):

    # initialize the variables
    parent_vector = np.zeros((constants.n_permutations, n_cities, constants.dimension))
    parent_distance = np.zeros(constants.n_permutations)

    # tournament loop
    for i in range(constants.n_tournaments):
        # select a number of individuals with uniform distribution
        tournament_individuals = np.random.random_integers(0, constants.n_permutations - 1, size=constants.n_individuals)

        # Select the distance of those individuals
        tournament_distance = np.zeros(constants.n_individuals)
        for j in range(constants.n_individuals):
            tournament_distance[j] = distance_vector[tournament_individuals[j]]

        # chose the individual with the smallest distance
        min_distance = min(tournament_distance)
        index = np.where(tournament_distance == min_distance)

        # build the parent vector and parent distance
        parent_vector[i, :, :] = individuals_vector[index[0][0], :, :]
        parent_distance[i] = min_distance

    return parent_vector, parent_distance


     


