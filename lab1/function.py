import sympy as sp
import numpy as np

from numpy.linalg import norm, inv, det
import matplotlib.pyplot as plt
import matplotlib.colors as colors

class GoalFunction:
    def __init__(self, fun, minim = (1,1)): 
        x, y = sp.symbols('x y')
        self.fun = fun
        self.minim = minim
        self.grad = np.array([sp.diff(self.fun(x,y),x,1), 
                                sp.diff(self.fun(x,y),y,1)]) 
        self.hes = np.array([[sp.diff(self.grad[0],x,1), sp.diff(self.grad[0],y,1)],
                            [sp.diff(self.grad[1],x,1), sp.diff(self.grad[1],y,1)]])
    def gradient(self, pnt:np.array):
        xi, yi = pnt[0], pnt[1]
        x, y = sp.symbols('x y')
        return np.array([self.grad[0].subs({x:xi, y: yi}), 
                    self.grad[1].subs({x:xi, y: yi})], dtype = 'double')
    

    def hesjan(self, pnt: np.array):
        x, y = sp.symbols('x y')
        xi, yi = pnt[0], pnt[1]
        return np.array([[self.hes[0,0].subs({x:xi, y: yi}), 
                        self.hes[0,1].subs({x:xi, y: yi})],
                        [self.hes[1,0].subs({x:xi, y: yi}), 
                        self.hes[1,1].subs({x:xi, y: yi})]], dtype = 'double')

    def plot_function(self):
        fig = plt.figure(figsize=(7,7))
        ax = plt.axes()
        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)
        X, Y = np.meshgrid(x, y)
        Z = self.fun(X, Y)
        pcm = ax.pcolor(X, Y, Z,
                norm=colors.LogNorm(vmin=Z.min(), vmax=Z.max()),
                cmap='magma', shading='auto')
        plt.xlabel('x')
        plt.ylabel('y')
        ax.plot(self.minim[0], self.minim[1],'c*', markersize = 15)
        plt.title("Funkcja celu")
        fig.colorbar(pcm)
        plt.tight_layout()
        plt.savefig('goal_fun') 

    
    def print_info(self):
        print(f"Gradient to: \n\tdx: {self.grad[0]} \n\tdy: {self.grad[1]}")
        print(f"Hesjan to: \n\tdxx: {self.hes[0,0]} \n\tdxy: {self.hes[0,1]} \n\tdyx: {self.hes[1,0]} \n\tdyy: {self.hes[1,1]}")


def goal_fun(x: float, y: float):
    return (1-x)**2 + 100*(y-x*x)**2


