import constants

import numpy as np


def random_vector_generator_function(n_points):
    """
    This function generates a random vector with the coordinates of the points

    :param n_points: number of points
    :return: vector: vector containing the points coordinates
    """
    # set the seed of the random function to avoid errors in the vector generator
    np.random.seed(2)

    vector = np.zeros((n_points, constants.dimension))
    for i in range(n_points):
        vector[i] = np.random.rand(2) * constants.square_size


    return vector

