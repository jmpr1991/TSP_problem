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

    # intialize variables for statistical analysis
    all_parent_vectors = np.zeros((constants.n_executions, constants.n_permutations, constants.n_cities, constants.dimension))
    all_parent_distances = np.zeros((constants.n_executions, constants.n_permutations))
    all_min_distances = []
    all_mean_distances = []
    all_std_distances = []
    total_generations = []

    # initialize success rate and success mean evaluations number parameters
    success_rate = 0
    pex = []

    # create the initial vector with cities
    vector = rand_vect.random_vector_generator_function(constants.n_cities)

    for execution_i in range(constants.n_executions):
        print("execution {}".format(execution_i+1), "on going")

        # initialize the population shuffling the vector with cities
        parent_vector, parent_distance = initialization.initialization_function(vector, constants.n_cities)

        # initialize variables
        min_distance = []
        mean_distance = []
        std_distance = []
        number_generations = 0
        termination_generation = 0

        # generation evolution loop
        while number_generations < constants.n_generations:

            # parent selection
            parent_sel_vector, parent_sel_distance = parent_selection.parent_selection_function(parent_vector, parent_distance, constants.n_cities)

            # crossover
            child_vector, child_distance = crossover.crossover_function(parent_sel_vector, parent_sel_distance, constants.n_cities)

            # mutation
            child_mutated_vector, child_mutated_distance = mutation.mutation_function(child_vector, child_distance, constants.n_cities)

            # survival selections and elitism
            new_parent_vector, new_parent_distance = survival_elitism.survival_elitism_function(child_mutated_vector, child_mutated_distance, parent_vector, parent_distance)

            # compute the min distance and mean distance
            min_distance.append(min(new_parent_distance))
            mean_distance.append(np.mean(new_parent_distance))
            std_distance.append(np.std(new_parent_distance))

            # compute termination condition if best individual does not change for a number of generations
            if min(new_parent_distance) == min(parent_distance):
                # check convergence
                termination_generation = termination_generation + 1
                if termination_generation == constants.end_condition:
                    total_generations.append(number_generations)
                    parent_vector = new_parent_vector
                    parent_distance = new_parent_distance
                    break

                #check if the optimum distance has been achieved (only for the square shaped cities)
                if constants.square_cities:
                    if min(new_parent_distance) <= constants.square_size * 4 + constants.delta:
                        total_generations.append(number_generations)
                        parent_vector = new_parent_vector
                        parent_distance = new_parent_distance
                        break
            else:
                termination_generation = 0

            # create next generation
            number_generations = number_generations + 1
            parent_vector = new_parent_vector
            parent_distance = new_parent_distance

        # save values for statistical analysis
        all_parent_vectors[execution_i,:,:,:] = parent_vector
        all_parent_distances[execution_i, :] = parent_distance
        all_min_distances.append(min_distance)
        all_mean_distances.append(mean_distance)
        all_std_distances.append(std_distance)

        # compute success rate if square shaped city
        if constants.square_cities:
            if all_min_distances[execution_i][-1] <= 4 * constants.square_size + constants.delta:
                success_rate = success_rate + 1
                pex.append(number_generations)

    # Success rate computation
    print("\n Statistics:")
    if constants.square_cities:
        print("TE = ", success_rate/constants.n_executions * 100, "%")
        if success_rate  == 0:
            print("PEX = n/a")
        else:
            print("PEX = ", np.mean(pex), " +/-", np.std(pex))

    # VAMM computation
    vam = np.zeros(constants.n_executions)
    for i in range(constants.n_executions):
        vam[i] = float(min(np.array(all_min_distances[i])))

    vamm = sum(vam)/constants.n_executions
    vamm_std = np.std(vam)
    print('VAMM = ', vamm, '+/-', vamm_std)
    print('Execution mean number to converge = ', np.mean(total_generations), '+/-', np.std(total_generations))

    min_index = np.argmin(all_parent_distances[0, :])
    plt.plot(np.append(all_parent_vectors[0, min_index, :, 0],all_parent_vectors[0, min_index, 0, 0]),
                    np.append(all_parent_vectors[0, min_index, :, 1], all_parent_vectors[0, min_index, 0, 1]))
    plt.show()

    # print the convergence of the best individual
    plt.plot(np.array(all_min_distances[0]), linewidth=0.5)
    plt.plot(np.array(all_mean_distances[0]), linewidth=0.5)
    plt.fill_between([i for i in range(np.size(np.array(all_mean_distances[0])))],
                     np.array(all_mean_distances[0]) - np.array(all_std_distances[0]),
                     np.array(all_mean_distances[0]) + np.array(all_std_distances[0]), alpha=0.3, label='error bar')
    plt.title('Progress curve of the best individual of each generation')
    plt.xlabel('Generation')
    plt.ylabel('Adaptation function (distance)')
    plt.legend(['best individual', 'population mean', 'error band'])
    plt.show()



if __name__ == "__main__":
    main()



