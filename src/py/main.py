import tsplib95


def getMatrix(problem):
    dimension = len(list(problem.get_nodes()))
    edges = list(problem.get_edges())

    mat = [[None for _ in range(dimension)] for _ in range(dimension)]

    for edge in edges:
        mat[edge[0] - 1][edge[1] - 1] = problem.get_weight(*edge)

    return mat

problem = tsplib95.load('../data/gr120.tsp')
print(type(problem))

mat = getMatrix(problem)
print(mat)