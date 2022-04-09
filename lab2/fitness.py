import numpy as np
from typing import List
def fitness(genome : np.array, problem : np.array) -> int:
    problem_c = problem.copy()

    for g in range(len(genome)):
        if genome[g] == 1:
            problem_c[:,g] = 0 
            problem_c[g,:] = 0 

    if np.sum(problem_c) != 0: 
        return len(genome) + 1 + np.sum(problem_c) 
    else: 
        return np.sum(genome) 


def population_fitness(population: List[np.array], problem: np.array) -> List[float]:
    return [fitness(genome, problem) for genome in population]

def evaluate_solution(genome: np.array, problem: np.array):
    problem_c = problem.copy()
    for g in range(len(genome)):
        if genome[g] == 1:
            problem_c[:,g] = 0
            problem_c[g,:] = 0
    
    return problem_c, np.sum(problem_c) == 0
