import networkx as nx
import random
import pickle


def graph_generator(size: int, type:str = 'complete'):
    if type == 'complete':
        p = nx.complete_graph(size)
        
    elif type == 'bipart':
        if size%2 == 0:
            p = nx.complete_bipartite_graph(int(size*0.5),int(size*0.5))
        else:
            p = nx.complete_bipartite_graph(int(size*0.5)+1,int(size*0.5))
    elif type == 'removed':
        p = nx.complete_graph(size)
        edges = list(p.edges())
        random_edges = random.choices(edges, k = int(0.5 * len(edges)))
        p.remove_edges_from(random_edges)
        while not nx.is_connected(p):
            p = nx.complete_graph(size)
            edges = list(p.edges())
            random_edges = random.choices(edges, k = int(0.5 * len(edges)))
            p.remove_edges_from(random_edges)

    problem = nx.convert_matrix.to_numpy_array(p)
    return problem


