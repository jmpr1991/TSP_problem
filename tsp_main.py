import constants
import random_vector_generator as rand_vect
import initialization
import parent_selection
import crossover
import mutation
import survival_elitism

import numpy as np
import matplotlib.pyplot as plt


def main():

    n_cities = 100

    # create the initial vector with cities
    vector = rand_vect.random_vector_generator_function(n_cities)
    print("vector inicial")
    print(vector)

    # initialize the population shuffling the vector with cities
    parent_vector, parent_distance = initialization.initialization_function(vector, n_cities)
    print("primera poblacion")
    print(parent_vector)
    print(parent_distance)

    # initialize variables
    min_distance = []
    mean_distance = []
    number_generations = 0
    termination_generation = 0

    # generation evolution loop
    while number_generations <= constants.n_generations:

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
        new_parent_vector, new_parent_distance = survival_elitism.survival_elitism_function(child_mutated_vector, child_mutated_distance, parent_vector, parent_distance)
        print("selection\n")
        print(new_parent_vector)
        print(new_parent_distance)

        # compute the min distance and mean distance
        min_distance.append(min(new_parent_distance))
        mean_distance.append(np.mean(new_parent_distance))

        # compute termination condition if best individual does not change for 100 generations
        if (min(new_parent_distance) - min(parent_distance)) == 0:
            termination_generation = termination_generation + 1
            if termination_generation == 100:
                break
        else:
            termination_generation = 0


        # create next generation
        number_generations = number_generations + 1
        parent_vector = new_parent_vector
        parent_distance = new_parent_distance



    print("min distance")
    print(np.array(min_distance))
    print(np.array(mean_distance))

    plt.plot(min_distance)
    plt.plot(mean_distance)
    plt.show()

if __name__ == "__main__":
    main()



