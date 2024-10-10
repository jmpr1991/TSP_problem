import numpy as np


def evaluation_function(vector_list):
    """
    this function evaluates the sum of distances of the point of an array
    :param vector_list: vector with the coordinates of the different point
    :return: distance: total distance
    """

    distance = 0
    for i in range(np.size(vector_list, 0)):

        # compute the distance between elements of the vecto until arriving to the first element
        if i != np.size(vector_list, 0) - 1:
            distance = distance + np.sqrt((vector_list[i][0]**2 - vector_list[i+1][0])**2 +
                                          (vector_list[i][1]**2 - vector_list[i+1][1])**2)
        else:
            distance = distance + np.sqrt((vector_list[i][0]**2 - vector_list[0][0])**2 +
                                          (vector_list[i][1]**2 - vector_list[0][1])**2)

    return distance




