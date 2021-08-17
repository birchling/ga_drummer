import numpy as np
import scipy as sci
import time
import random
import matplotlib.pyplot as plt

class Individual():
    def __init__(self, allow_aging):
        self.genome = np.zeros(96)
        self.fitness = 0
        self.age = 0
        self.decay = 0.001
        self.allow_aging = allow_aging

        for index, _ in enumerate(self.genome):
            res = random.random()
            #print(res)
            if (0.5 > res):
                self.genome[index] = int(1)
            else:
                self.genome[index] = int(0)
        self.genome = self.genome.astype("int") 

    def __repr__(self):
        return repr((self.genome, self.fitness, self.age, self.decay))
    
    def get_fitness(self, target):
        if self.allow_aging:
            #Check that arrays are the same length
            if len(self.genome) != len(target):
                raise(Exception)
            #Determine new individuals fitness
            if self.age == 0:
                self.fitness = 0 # Reset fitness
                for index, chromosome in enumerate(self.genome):
                    if chromosome == target[index]:
                        self.fitness += 1
        else:
            self.fitness = 0 # Reset fitness
            for index, chromosome in enumerate(self.genome):
                if chromosome == target[index]:
                    self.fitness += 1
    
    #Reduce fitness of older individuals
    def ageing(self):
        self.age += 1
        if self.age > 50:
            self.fitness = self.fitness - (self.fitness * self.decay)

    

class Population:
    individuals = []
    generation = 0
    max_generation = 1000
    mutation_rate = 0.1
    best = None

    def __init__(self, pop_size, aging):
        for _ in range(pop_size):
            ind = Individual(aging)
            self.individuals.append(ind)
            self.aging = aging
    def crossover(self):
        #Replace the least fit half with offspring of the fittest half for crossover
        quater_of_individuals = int(len(self.individuals)/4)
        for index in range(0, quater_of_individuals, 2):
            #print(index)
            #first offspring
            for gene in range(0, len(self.individuals[0].genome)-1, 2):
                #print(self.individuals[(-1 * index) - 1].genome)
                self.individuals[(-1 * index) - 1].genome[gene] = self.individuals[index].genome[gene + 1]
                self.individuals[(-1 * index) - 1].genome[gene + 1] = self.individuals[index + 1].genome[gene]
                #print(self.individuals[(-1 * index) - 1].genome)
                self.individuals[(-1 * index) - 2].genome[gene] = self.individuals[index].genome[gene]
                self.individuals[(-1 * index) - 2].genome[gene + 1] = self.individuals[index + 1].genome[gene + 1]
            #print(self.individuals[(-1 * index) - 1].genome)
            #self.individuals[(-1 * index) - 1].genome[1::2] = self.individuals[index].genome[::2]
            #self.individuals[(-1 * index) - 1].genome[::2] = self.individuals[index + 1].genome[1::2]
            #self.individuals[(-1 * index) - 1].age = 0
            ##second offspring
            #self.individuals[(-1 * index) - 2].genome[::2] = self.individuals[index].genome[::2]
            #self.individuals[(-1 * index) - 2].genome[1::2] = self.individuals[index + 1].genome[1::2]
            #self.individuals[(-1 * index) - 2].age = 0

    def sort_by_fitness(self):
        self.individuals = sorted(self.individuals, key=lambda individual: individual.fitness, reverse=True)

    def mutation(self):
        for individual in self.individuals:
            for gene in individual.genome:
                if(random.random() < self.mutation_rate):
                    if gene == 0:
                        gene = 1
                    else:
                        gene = 0


def main():
    #Beat of funky drummer encoded
    #one line = one beat
    funky_drummer = [1,0,1,1,0,0,1,0,1,1,0,0,
                    1,0,0,1,0,0,0,0,0,1,1,0,
                    1,0,1,1,1,0,1,0,1,1,1,0,
                    1,1,0,0,0,1,1,0,0,1,0,0,
                    1,0,1,1,0,0,1,0,1,1,0,0,
                    1,1,0,1,0,0,0,0,0,1,1,0,
                    1,0,1,1,1,0,1,0,1,1,1,0,
                    1,1,0,0,0,1,1,0,0,1,0,0]
    funky = np.array(funky_drummer)
    optimum = len(funky_drummer)
    
    #Generate population
    pop = Population(80, True)
    generations = []
    best_fitnesses = []
    while(pop.generation < pop.max_generation):
        #Get fitness
        for individual in pop.individuals:
            #print(individual.__dict__)
            individual.get_fitness(funky)
            if pop.aging:
                individual.ageing()
        pop.sort_by_fitness()
        pop.crossover()
        
        if pop.best == None:
            pop.best = pop.individuals[0]
        elif pop.best.fitness < pop.individuals[0].fitness:
            print(pop.individuals[0].fitness)
            pop.best = pop.individuals[0]
        if pop.best.fitness == optimum:
            break
        pop.mutation()
        pop.generation += 1
        generations.append(pop.generation)
        best_fitnesses.append(pop.best.fitness)
    print(pop.best.fitness)
    print(pop.best.genome)
    print(pop.generation)
    plt.plot(generations, best_fitnesses)
    saveName = 'with_aging_' + str(2) + '.png'
    plt.savefig(saveName)
    plt.close()
if __name__ == "__main__":
    main()