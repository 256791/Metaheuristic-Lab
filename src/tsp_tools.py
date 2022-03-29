import numpy as np
import tsplib95
import matplotlib.pyplot as plt
import networkx as nx
from enum import Enum


class InstanceType(Enum):
    SYMETRIC = 1
    ASYMETRIC = 2
    EUC2D = 3


def header(filename, filetype, description, dimension, edgeWeightType):
    return f"NAME: {filename}\n" +\
        f"TYPE: {filetype}\n" +\
        f"COMMENT: {description}\n" +\
        f"DIMENSION: {dimension}\n" +\
        f"EDGE_WEIGHT_TYPE: {edgeWeightType}\n"


def to_atsp(filename, mat, dimension, description, maxVal):
    f = open(f"./data/{filename}.atsp", "w")
    f.write(header(filename, "ATSP", description, dimension, "EXPLICIT"))
    f.write("EDGE_WEIGHT_FORMAT: FULL_MATRIX\n")
    f.write("EDGE_WEIGHT_SECTION\n")

    maxLen = len(str(maxVal)) + 3

    for y in mat:
        for x in y:
            curLen = len(str(x))
            f.write(" " * (maxLen - curLen))
            f.write(str(x))
        f.write("\n")

    f.write("EOF\n")
    f.close()
    return None


def to_tsp(filename, coords, dimension, description, maxVal):
    f = open(f"./data/{filename}.tsp", "w")
    f.write(header(filename, "TSP", description, dimension, "EUC_2D"))
    f.write("NODE_COORD_SECTION\n")

    for i in range(dimension):
        f.write(f"{i + 1} {coords[i][0]}.0 {coords[i][1]}.0\n")

    f.write("EOF\n")
    f.close()
    return None


def gen_random_instance(filename, dimension, instanceType=InstanceType.SYMETRIC, description="none", minVal=0, maxVal=50):
    if(instanceType == InstanceType.EUC2D):
        mat = np.random.random_integers(minVal, maxVal, (dimension, 2))
        to_tsp(filename, mat, dimension, description, maxVal)
        return mat

    mat = np.random.random_integers(minVal, maxVal, (dimension, dimension))
    for i in range(0, dimension):
        mat[i][i] = maxVal*100

    if(instanceType == InstanceType.SYMETRIC):
        for i in range(0, dimension):
            for j in range(0, i):
                mat[i][j] = mat[j][i]
        to_atsp(filename, mat, dimension, description, maxVal)
        return mat

    if(instanceType == InstanceType.ASYMETRIC):
        to_atsp(filename, mat, dimension, description, maxVal)
        return mat


def get_matrix(problem):
    dimension = len(list(problem.get_nodes()))
    edges = list(problem.get_edges())

    mat = [[None for _ in range(dimension)] for _ in range(dimension)]

    for edge in edges:
        mat[edge[0] - 1][edge[1] - 1] = problem.get_weight(*edge)

    return mat





# if intended to write function insead using trace_tours()

# def get_cost(problem):
#     res = []
#     for tour in problem.tours:
#         cost = 0
#         for i in range(0, len(tour)-1):
#             cost += problem.get_weight(tour[i], tour[i+1])
#         cost += problem.get_weight(tour[-1],tour[0])
#         res.append(cost)
#     return res


# def random_solve(problem):
#     nodes = np.array(list(problem.get_nodes()))
#     np.random.shuffle(nodes[1:-1])
#     problem.tours.append(nodes.tolist())


def print_tour(problem, tour_n=0, weights=False):
    G = nx.Graph()
    pos = None

    if problem.edge_weight_type == 'EUC_2D':
        for node in list(problem.get_nodes()):
            G.add_node(node, coord=problem.node_coords[node])
        pos = nx.get_node_attributes(G, 'coord')
    else:
        G.add_nodes_from(list(problem.get_nodes()))
        pos = nx.spring_layout(G, seed=225)

    tour = problem.tours[tour_n]
    for i in range(0, len(tour)-1):
        G.add_edge(tour[i], tour[i+1],
                   weight=problem.get_weight(tour[i], tour[i+1]))
    G.add_edge(tour[-1], tour[0], weight=problem.get_weight(tour[-1], tour[0]))

    nx.draw(G, pos)
    if weights:
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()


def print_graph(problem, weights=False):
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


def PRD(problem, tour, opt):
    return 100 * (problem.trace_tours([tour])[0] - problem.trace_tours([opt])[0]) / problem.trace_tours([opt])[0]