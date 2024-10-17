import constants

import numpy as np

def survival_elitism_function(child_mutated_vector, child_mutated_distance, parent_vector, parent_distance):

    #select the best individual of the  current population if this condition is met
    if min(parent_distance) < min(child_mutated_distance):
        #select the best individual of the parent vector
        min_distance = min(parent_distance)
        index_best_individual = np.where(parent_distance == min_distance)[0][0]
        best_individual = parent_vector[index_best_individual, :, :]

        #select the worst individual of the current generation
        max_distance = max(child_mutated_distance)
        index_worst_individual = np.where(child_mutated_distance == max_distance)[0][0]
        worst_individual = child_mutated_vector[index_worst_individual, :, :]

        # create new generation
        parent_vector = child_mutated_vector
        parent_vector[worst_individual,:, :] = best_individual
        parent_distance[worst_individual,:, :] = min_distance

    # create the new generation without elitism
    else:
        parent_vector = child_mutated_vector
        parent_distance = child_mutated_distance

    return parent_vector, parent_distance