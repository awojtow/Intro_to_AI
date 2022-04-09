
import random
import numpy as np
from typing import List

 
import random
import numpy as np
from typing import List


 
def mutate_one(genom : np.array, prob1 : float) -> np.array:
    n_mutate = max(1,int(len(genom) * prob1))
    mutate = np.zeros(len(genom))
    mutate[:n_mutate] = 1
    np.random.shuffle(mutate)
    return np.abs(genom - mutate)

def mutation(population : List[np.array], prob0: float, prob1 : float, mutate_one = mutate_one) -> List[np.array]:
    new_population = []
    for genom_i in range(len(population)):
        if random.random() > prob0:
            new_population.append(mutate_one(population[genom_i], prob1))
        else:
            new_population.append(population[genom_i])
    return new_population


