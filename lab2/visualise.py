import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from fitness import evaluate_solution
def visualise(problem: np.array, solution: np.array, name: str = 'name', title:str = None, pos = None):
    G = nx.from_numpy_matrix(problem, parallel_edges=True, create_using=nx.MultiGraph)
    pc, eval = evaluate_solution(solution, problem)
    S = nx.from_numpy_matrix(pc, parallel_edges=True, create_using=nx.MultiGraph)
    
    if pos == None:
        pos=nx.spring_layout(G)
    plt.figure()
    if title:
        plt.suptitle(title)
    plt.title(f"Covers all:  {eval} \n Nodes: {int(np.sum(solution))}", size = 9)
    nx.draw(G, cmap = plt.get_cmap('jet'), with_labels = True, node_color = ['green' if i == 1 else 'red' for i in solution], edge_color = ['red' if i in S.edges() else 'green' for i in G.edges()], pos = pos)
    plt.tight_layout()
    plt.savefig(name)
    return pos

def plot_history(history:dict, name:str = 'history', title:str = None):
    minimas = [v[0] for v in history.values()]
    scores = [v[1] for v in history.values()]
    means = np.array([np.mean(v) for v in scores])
    std = np.array([np.std(v) for v in scores])
    plt.figure()
    if title:
        plt.suptitle(title)
    plt.title(f"Minimal value first found at {minimas.index(min(minimas))}")
    plt.plot(history.keys(), minimas, label = 'global minimum fit')
    plt.plot(history.keys(), means, label = 'mean fit')
    plt.plot(history.keys(), means - std, 'r--')
    plt.plot(history.keys(), means + std, 'r--', label = 'mean fit +- std')
    plt.legend()
    plt.savefig(name + "_minimas")

