from pyclbr import Function
import random
import numpy as np
from typing import List
from fitness import fitness


def select_one(population : List[np.array], problem: np.array, tournament_size : int, fitness_func = fitness) -> np.array:
    chosen =  random.choices(population, k = tournament_size)
    return min(chosen, key=lambda c: fitness_func(c, problem))

def selection(population : List[np.array],  problem: np.array, tournament_size : int = 2, fitness_func = fitness, select_one = select_one) -> List[np.array]:
    new_population = []
    for i in range(len(population)):   
        new_population.append(select_one(population, problem, tournament_size, fitness_func))
    return new_population

