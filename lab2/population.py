import numpy as np
from typing import List


def generate_one(size:int) -> np.array:
    return np.random.choice([0, 1], size=size)
    
def generate_population(number :int, size: int, generate_one = generate_one) -> List[np.array]:
    return [generate_one(size) for i in range(number)]

