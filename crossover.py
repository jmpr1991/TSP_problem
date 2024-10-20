import constants
import evaluation

import numpy as np

def crossover_function(parent_vector, parent_distance, n_cities):
    """
    This function recombinates the different parent vectors with the Partially Mapped Crossover method
    :param parent_vector: input vector
    :param parent_distance: input distance
    :param n_cities: vector size
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
        # generate a crossover probability with uniform distribution
        crossover_prob_i = np.random.uniform(0.0,1.0)

        # generate the segment for crossover avoiding the edges
        s0 = np.random.randint(2,n_cities - 2)
        sf = np.random.randint(s0 + 1,n_cities - 1)

        # select the parents to recombinate and delete them from the list to avoid repetition
        parents_crossover = np.zeros(constants.n_individuals, int)
        for k in range(constants.n_individuals):
            parents_crossover[k] = np.random.choice(list_parents)
            list_parents.remove(int(parents_crossover[k]))

        # perform the crossover if the following condition is met
        if crossover_prob_i <= constants.pc:
            # create the first child
            child_vector[n_children, s0-1:sf, :] = parent_vector[parents_crossover[0], s0-1:sf, :]

            # save the remaining elements in a vector
            left_elements = parent_vector[parents_crossover[0],
                            np.concatenate(([i for i in range(0,s0-1)], [i for i in range(sf, n_cities)])), :]

            # iterate the pending elements
            #index = np.zeros(np.size(left_elements, axis=0))
            last_elements = []
            for i in range(np.size(left_elements,0)):
                if left_elements[i]  not in parent_vector[parents_crossover[1], s0-1:sf, :]:
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

            # create the second child
            child_vector[n_children, s0-1:sf, :] = parent_vector[parents_crossover[1], s0-1:sf, :]

            # save the remaining elements in a vector
            left_elements = parent_vector[parents_crossover[1],
                            np.concatenate(([i for i in range(0,s0-1)], [i for i in range(sf, n_cities)])), :]

            # iterate the pending elements
            #index = np.zeros(np.size(left_elements, axis=0))
            last_elements = []
            for i in range(np.size(left_elements,0)):
                if left_elements[i]  not in parent_vector[parents_crossover[0], s0-1:sf, :]:
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

        # clone the parents if the following condition is met
        else:
            #clone parent 1
            child_vector[n_children, :, :] = parent_vector[parents_crossover[0], :, :]
            child_distance[n_children] = parent_distance[parents_crossover[0]]
            n_children = n_children + 1

            # clone parent 2
            child_vector[n_children, :, :] = parent_vector[parents_crossover[1], :, :]
            child_distance[n_children] = parent_distance[parents_crossover[1]]
            n_children = n_children + 1

    return child_vector, child_distance
