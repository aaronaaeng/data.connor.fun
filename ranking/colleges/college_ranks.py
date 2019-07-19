import numpy as np
import networkx as nx


def spring_rank(G):
    G = np.array(G)
    k_in = np.sum(G, 0)
    k_out = np.sum(G, 1)
    
    K = np.diag(k_out + k_in)
    A = K - (G + G.T)
    B = k_out - k_in
        
    return np.transpose(np.linalg.lstsq(A, B, rcond=None)[0])

def main():
    G = nx.read_edgelist('data/edge_list.txt', create_using=nx.MultiDiGraph)


if __name__ == '__main__':
    main()