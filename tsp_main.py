import constants
import random_vector_generator as rand_vect
import evaluation
import initialization
import parent_selection
import crossover
import mutation
import survival_elitism

import numpy as np


def main():

    n_cities = 10

    # create the initial vector with cities
    vector = rand_vect.random_vector_generator_function(n_cities)
    print("vector inicial")
    print(vector)

    # initialize the population shuffling the vector with cities
    parent_vector, parent_distance = initialization.initialization_function(vector, n_cities)
    print("primera poblacion")
    print(parent_vector)
    print(parent_distance)



    # parent selection
    parent_sel_vector, parent_sel_distance = parent_selection.parent_selection_function(parent_vector, parent_distance, n_cities)
    print("padre\n")
    print(parent_sel_vector)
    print(parent_sel_distance)

    # crossover
    child_vector, child_distance = crossover.crossover_function(parent_sel_vector, parent_sel_distance, n_cities)
    print("child\n")
    print(child_vector)
    print(child_distance)

    # mutation
    child_mutated_vector, child_mutated_distance = mutation.mutation_function(child_vector, child_distance, n_cities)
    print("mutation\n")
    print(child_mutated_vector)
    print(child_mutated_distance)

    # survival selections and elitism
    parent_vector, parent_distance = survival_elitism.survival_elitism_function(child_mutated_vector, child_mutated_distance, parent_vector, parent_distance)
    print("selection\n")
    print(parent_vector)
    print(parent_distance)


if __name__ == "__main__":
    main()



