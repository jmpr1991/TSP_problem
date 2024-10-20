import constants

import numpy as np


def random_vector_generator_function(n_points):
    """
    This function generates a random vector with the coordinates of the points

    :param n_points: number of points
    :return: vector: vector containing the points coordinates
    """

    vector = np.zeros((n_points, constants.dimension))
    for i in range(n_points):
        #vector[i] = np.random.rand(2) * constants.square_size
        axis = np.random.randint(0,4)
        if axis == 0:
            vector[i] = [0, float(np.random.rand(1,1) * constants.square_size)]
        elif axis == 1:
            vector[i] = [float(np.random.rand(1)) * constants.square_size, 0]
        elif axis == 2:
            vector[i] = [float(np.random.rand(1)) * constants.square_size, 1]
        elif axis== 3:
            vector[i] = [1, float(np.random.rand(1) * constants.square_size)]

    return vector

