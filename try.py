import networkx as nx
import matplotlib.pyplot as plt
# independent set problem
def indenpend():
    # create a graph
    G = nx.Graph()
    # add nodes
    G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    # add edges
    G.add_edges_from([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (6, 7), (6, 8), (6, 9), (6, 10), (7, 8), (7, 9), (7, 10), (8, 9), (8, 10), (9, 10)])
    # find the independent set
    ind = nx.maximal_independent_set(G)
    # print the independent set
    print(ind)
    # draw the graph
    nx.draw(G)
    # show the graph
    plt.show()