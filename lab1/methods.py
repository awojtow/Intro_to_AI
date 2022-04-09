
from numpy.linalg import norm, inv, solve
import numpy as np
import matplotlib.pyplot as plt
from function import GoalFunction
from time import process_time
import matplotlib.colors as colors

class Method:
    def __init__(self, beta: float, max_iter: int, init_point: list, fun: GoalFunction, name: str = 'method', eps: float = 10E-12):
        self.beta = beta
        self.max_iter = max_iter
        self.fun = fun
        self.done_iter = None
        self.init_point = init_point
        self.eps = eps
        self.pos = []
        self.time = None
        self.name = name
        
    def print_info(self):
        print(f"done {self.done_iter}/{self.max_iter} iterations")
        print(f"cords {self.pos[-1]}, \nfinal value {self.fun.fun(self.pos[-1][0], self.pos[-1][1])}, \nfinal gradient {self.fun.gradient(self.pos[-1])}")
        print(f"time {self.time}")


class NewtonMethod(Method):
    def search(self):
        start = process_time()
        cords = np.array(self.init_point)
        iter = 0
        value_diff = self.eps + 1
        while iter < self.max_iter and value_diff > self.eps:
            self.pos.append(cords)
            d = np.dot(inv(self.fun.hesjan(cords)),self.fun.gradient(cords))
            value = self.fun.fun(cords[0], cords[1])
            cords = cords - self.beta * d
            value_diff = abs(value - self.fun.fun(cords[0], cords[1]))
            iter+=1
        end = process_time()
        self.done_iter = iter
        self.time = end - start

class GradientDescent(Method):
    def search(self):
        start = process_time()
        cords = np.array(self.init_point)
        iter = 0
        value_diff = self.eps + 1 
        while iter < self.max_iter and value_diff > self.eps:
            self.pos.append(cords)
            d =  self.fun.gradient(cords)
            value = self.fun.fun(cords[0], cords[1])
            cords = cords - self.beta * d
            value_diff = abs(value - self.fun.fun(cords[0], cords[1]))
            iter+=1
        end = process_time()
        self.done_iter = iter
        self.time = end - start
    
