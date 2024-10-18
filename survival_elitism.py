import constants

import numpy as np

def survival_elitism_function(child_mutated_vector, child_mutated_distance, parent_vector, parent_distance):
    """
    This function creates the new generation with elitism, substituting the worst individual of the new generation with
     the best individual of the current generation and
    :param child_mutated_vector: input vector
    :param child_mutated_distance: input distance
    :param parent_vector: new generation vector
    :param parent_distance: new generation distance
    :return: new_parent_vector: new generation vector
    :return: new generation distance
    """

    #select the best individual of the  current population if this condition is met
    if min(parent_distance) < max(child_mutated_distance):
        #select the best individual of the parent vector
        min_distance = min(parent_distance)
        index_best_individual = np.where(parent_distance == min_distance)[0][0]
        best_individual = parent_vector[index_best_individual, :, :]

        #select the worst individual of the current generation
        max_distance = max(child_mutated_distance)
        index_worst_individual = np.where(child_mutated_distance == max_distance)[0][0]

        # create new generation
        new_parent_vector = child_mutated_vector
        new_parent_vector[index_worst_individual,:, :] = best_individual
        new_parent_distance = child_mutated_distance
        new_parent_distance[index_worst_individual] = min_distance

    # create the new generation without elitism
    else:
        new_parent_vector = child_mutated_vector
        new_parent_distance = child_mutated_distance

    return new_parent_vector, new_parent_distance