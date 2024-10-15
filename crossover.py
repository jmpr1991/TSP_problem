import constants

import numpy as np

def crossover_function(parent_vector, parent_distance, n_cities):
    """
    This function recombinates the different parent vectors with the Partially Mapped Crossover method
    :param parent_vector:
    :param parent_distance:
    :param n_cities:
    :return:
    """

    # initialize the variables
    child_vector = np.zeros((constants.n_permutations, n_cities, constants.dimension))
    child_distance = np.zeros(constants.n_permutations)
    n_children = 0

    # loop to create the next generation
    while n_children < constants.n_permutations:
        #generate a crossover probability with uniform distribution
        crossover_prob_i = np.random.uniform(0.0,1.0)

        #select the parents for crossover
        parents_crossover = np.random.random_integers(0, constants.n_permutations - 1,
                                                      size=constants.n_individuals)

        # perform the crossover if the following condition is met
        if crossover_prob_i <= constants.pc:
            child_vector[n_children, constants.s0-1:constants.sf, :] = parent_vector[parents_crossover[0],
                                                                         constants.s0-1:constants.sf, :]

            # save the remaining elements in a vector
            left_elements = parent_vector[parents_crossover[0], [range(0,constants.s0-1), range(constants.sf,n_cities)], :]

            # iterate over the second parent
            for i in range(np.size(left_elements,0)):
                if left_elements[i]  not in parent_vector[parents_crossover[1], constants.s0-1:constants.sf-1, :]:
                    index = np.where(parent_vector[parents_crossover[1], :, :] == left_elements[i])
                    child_vector[n_children, index, :] = parent_vector[parents_crossover[0], index,:]
                    left_elements.remove(left_elements[i])