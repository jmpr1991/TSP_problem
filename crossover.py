import constants
import evaluation

import numpy as np

def crossover_function(parent_vector, parent_distance, n_cities):
    """
    This function recombinates the different parent vectors with the Partially Mapped Crossover method
    :param parent_vector:
    :param parent_distance:
    :param n_cities:
    :return: child_vector: vector with the parents recombination
    :return: child_distance: vector with the child distances
    """

    # initialize the variables
    child_vector = np.zeros((constants.n_permutations, n_cities, constants.dimension))
    child_distance = np.zeros(constants.n_permutations)
    n_children = 0
    list_parents = [i for i in range(constants.n_permutations)] # list parents for crossover

    # loop to create the next generation
    while n_children < constants.n_permutations:
        #generate a crossover probability with uniform distribution
        crossover_prob_i = np.random.uniform(0.0,1.0)

        #select different couple of parents for crossover
        #parents_crossover = np.random.random_integers(0, constants.n_permutations - 1,
                                                     # size=constants.n_individuals)

        #for i in range(constants.n_tournaments):
            # select 2 random individuals within the list and avoiding repetition
        parents_crossover = np.zeros(constants.n_individuals, int)
        for k in range(constants.n_individuals):
            parents_crossover[k] = np.random.choice(list_parents)
            list_parents.remove(int(parents_crossover[k]))

        # perform the crossover if the following condition is met
        if crossover_prob_i <= constants.pc:
            # create the first child
            child_vector[n_children, constants.s0-1:constants.sf, :] = parent_vector[parents_crossover[0], constants.s0-1:constants.sf, :]

            # save the remaining elements in a vector
            left_elements = parent_vector[parents_crossover[0],
                            np.concatenate(([i for i in range(0,constants.s0-1)], [i for i in range(constants.sf, n_cities)])), :]

            # iterate the pending elements
            #index = np.zeros(np.size(left_elements, axis=0))
            last_elements = []
            for i in range(np.size(left_elements,0)):
                if left_elements[i]  not in parent_vector[parents_crossover[1], constants.s0-1:constants.sf-1, :]:
                    index = np.where(parent_vector[parents_crossover[1], :, :] == left_elements[i])[0][0]
                    child_vector[n_children, int(index), :] = parent_vector[parents_crossover[1], int(index),:]
                else:
                    last_elements.append(left_elements[i])

            # iterate over last free elements
            if last_elements:
                for i in range(np.size(last_elements, 0)):
                    index = np.where(child_vector[n_children, :, :] == 0)[0][0]
                    child_vector[n_children, int(index), :] = last_elements[i]

            # evaluate the distance
            child_distance[n_children] = evaluation.evaluation_function(child_vector[n_children, :, :])

            # go to the next child
            n_children = n_children + 1

            # break condition
            if n_children == constants.n_permutations:
                break

            # create the second child
            child_vector[n_children, constants.s0-1:constants.sf, :] = parent_vector[parents_crossover[1], constants.s0-1:constants.sf, :]

            # save the remaining elements in a vector
            left_elements = parent_vector[parents_crossover[1],
                            np.concatenate(([i for i in range(0,constants.s0-1)], [i for i in range(constants.sf, n_cities)])), :]

            # iterate the pending elements
            #index = np.zeros(np.size(left_elements, axis=0))
            last_elements = []
            for i in range(np.size(left_elements,0)):
                if left_elements[i]  not in parent_vector[parents_crossover[0], constants.s0-1:constants.sf-1, :]:
                    index = np.where(parent_vector[parents_crossover[0], :, :] == left_elements[i])[0][0]
                    child_vector[n_children, int(index), :] = parent_vector[parents_crossover[0], int(index),:]
                else:
                    last_elements.append(left_elements[i])

            # iterate over last free elements
            if last_elements:
                for i in range(np.size(last_elements, 0)):
                    index = np.where(child_vector[n_children, :, :] == 0)[0][0]
                    child_vector[n_children, int(index), :] = last_elements[i]

            # evaluate the distance
            child_distance[n_children] = evaluation.evaluation_function(child_vector[n_children, :, :])

            # go to the next child
            n_children = n_children + 1

            # break condition
            if n_children == constants.n_permutations:
                break

        # clone the parents if the following condition is met
        else:
            #clone parent 1
            child_vector[n_children, :, :] = parent_vector[parents_crossover[0], :, :]
            child_distance[n_children] = parent_distance[parents_crossover[0]]
            n_children = n_children + 1
            # break condition
            if n_children == constants.n_permutations:
                break

            # clone parent 2
            child_vector[n_children, :, :] = parent_vector[parents_crossover[1], :, :]
            child_distance[n_children] = parent_distance[parents_crossover[1]]
            n_children = n_children + 1
            # break condition
            if n_children == constants.n_permutations:
                break





    return child_vector, child_distance
