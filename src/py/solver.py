import tsplib95
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


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


def random_solve(problem):
    nodes = np.array(list(problem.get_nodes()))
    np.random.shuffle(nodes[1:-1])
    problem.tours.append(nodes.tolist())


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


def PRD(problem, tour, opt):
    return 100 * (problem.trace_tours([tour])[0] - problem.trace_tours([opt])[0]) / problem.trace_tours([opt])[0]



if __name__ == '__main__':
    problem = tsplib95.load('../data/berlin52.tsp')
    opt = tsplib95.load('../data/berlin52.opt.tour')
    problem.tours = opt.tours

    random_solve(problem)
    print(opt.tours)
    print(problem.trace_tours(problem.tours))

    print_tour(problem)

    print(f'PRD = {PRD(problem, problem.tours[1], opt.tours[0])}%')
