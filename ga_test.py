import ga
import pytest
import numpy as np

def test_sort():
    pop = ga.Population(5, False)
    pop.individuals[0].fitness = 1
    pop.individuals[1].fitness = 2
    pop.individuals[2].fitness = 4
    pop.individuals[3].fitness = 3
    pop.individuals[4].fitness = 5
    pop.sort_by_fitness()
    assert pop.individuals[0].fitness == 5
    assert pop.individuals[1].fitness == 4
def test_crossover():
    pop = ga.Population(8, False)
    pop.individuals[0].genome = np.array([1,0,1,0,1,0,1,0])
    pop.individuals[1].genome = np.array([0,1,0,1,0,1,0,1])
    pop.individuals[2].genome = np.array([0,0,0,0,0,0,0,0])
    pop.individuals[3].genome = np.array([1,1,1,1,1,1,1,1])
    pop.individuals[4].genome = np.array([1,1,1,1,0,0,0,0])
    pop.individuals[5].genome = np.array([0,0,0,0,1,1,1,1])
    pop.individuals[6].genome = np.array([0,0,0,0,0,0,0,0])
    pop.individuals[7].genome = np.array([0,0,0,0,0,0,0,0])

    testVal = pop.individuals[0].genome[0::2]
    print("TEST VALUE")
    print(testVal)

    pop.crossover()
    
    assert pop.individuals[6].genome.all(1)
    assert pop.individuals[7].genome.all(0)
