import constants

import numpy as np
import os


def random_vector_generator_function(n_points):
    """
    This function generates a random vector with the coordinates of the points

    :param n_points: number of points
    :return: vector: vector containing the points coordinates
    """
    # set the seed of the random function to avoid errors in the vector generator
    np.random.seed(20)

    vector = np.zeros((n_points, constants.dimension))
    for i in range(n_points):
        vector[i] = np.random.rand(2) * constants.square_size

    # create new file with the vector
    # f = open(f'vector_cities_{n_points}', 'a')
    # f.write(str(vector))

    return vector

