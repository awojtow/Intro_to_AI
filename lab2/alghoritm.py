from population import generate_population
from fitness import *
from mutation import mutation
from selection import selection
import numpy as np
from time import process_time
from fitness import evaluate_solution
'''
Pseudokod  
P_t = init()
t = 0
ocena(P_t)
while !stop
    Tt = selekcja(Pt)
    Ot = mutacja(Tt)
    ocena(Ot)
    Pt = Ot
    t=t+1  
 '''

def genetic_alghoritm(problem: np.array, prob0: float, prob1 : float, iter_max: int, population_size: int , evaluate_solution  = evaluate_solution):
    history = {}
    start = process_time()
    curr_population = generate_population(number = population_size, size = problem.shape[0])
    curr_fitness = population_fitness(population = curr_population, problem = problem)
    curr_min =  min(curr_fitness)

    best_population = curr_population
    best_fitness = curr_fitness
    best_min = min(best_fitness)
    for iter in range(iter_max):
    
        Tt = selection(population = curr_population, problem = problem)
        Ot = mutation(Tt, prob0, prob1)

        curr_fitness = population_fitness(Ot,problem = problem)
        curr_population = Ot
        curr_min = min(curr_fitness)
        if curr_min > best_min:
            history[iter] = (best_min, curr_fitness)
        elif curr_min <= best_min:
            best_min = curr_min
            best_fitness = curr_fitness
            best_population = curr_population
            history[iter] = (best_min, curr_fitness)
    
    best_member = best_population[best_fitness.index(best_min)]
    end = process_time()
    pc, solution_eval = evaluate_solution(best_member, problem)
    return best_member, best_min, solution_eval,  end - start, history