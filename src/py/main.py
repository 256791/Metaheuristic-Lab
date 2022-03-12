import tsplib95
import matplotlib.pyplot as plt
import networkx as nx


def getMatrix(problem):
    dimension = len(list(problem.get_nodes()))
    edges = list(problem.get_edges())

    mat = [[None for _ in range(dimension)] for _ in range(dimension)]

    for edge in edges:
        mat[edge[0] - 1][edge[1] - 1] = problem.get_weight(*edge)

    return mat

def printGraph(problem, weights=False):
    G = problem.get_graph()
    print(G.nodes)
    if problem.edge_weight_type == 'EUC_2D':
        pos = nx.get_node_attributes(G, 'coord')
    else:
        pos = nx.spring_layout(G, seed=225)
    nx.draw(G, pos)
    if weights:
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()


if __name__ == '__main__':
    problem = tsplib95.load('../data/br17.atsp')
    print(type(problem))

    mat = getMatrix(problem)
    print(mat)

    printGraph(problem)