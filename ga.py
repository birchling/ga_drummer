import numpy as np
import scipy as sci
import time
import random

class Individual():
    def __init__(self):
        self.genome = np.zeros(96)
        self.fitness = 0
        self.age = 0
        self.decay = 0.05

        for index, _ in enumerate(self.genome):
            res = random.random()
            #print(res)
            if (0.5 > res):
                self.genome[index] = 1
            else:
                self.genome[index] = 0

    def get_fitness(self, target):
        #Check that arrays are the same length
        if len(self.genome) != len(target):
            raise(Exception)
        #Determine new individuals fitness
        if self.age == 0:
            fitness = 0 # Reset fitness
            for chromosome, index in enumerate(self.genome):
                if chromosome == target[index]:
                    fitness += 1
    
    #Reduce fitness of older individuals
    def ageing(self):
        self.age += 1
        if self.age > 5:
            self.fitness = self.fintness * self.decay

class Population:
    individuals = []
    generation = 0
    max_generation = 100
    best = None

    def __init__(self, pop_size):
        for i in range(pop_size):
            ind = Individual()
            self.individuals.append(ind)
#Generate population
pop = Population(20)
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
print(len(funky_drummer))

while(pop.generation < pop.max_generation):
    #Get fitness
    for individual in pop.individuals:
        #print(individual.__dict__)
        individual.get_fitness(funky)
        print(individual.fitness)
#Check genes
#for ind in pop.individuals:
#    print(ind.genome)