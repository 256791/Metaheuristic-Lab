import tsplib95
import sys

def get_matrix(problem):
    dimension = len(list(problem.get_nodes()))
    edges = list(problem.get_edges())

    mat = [[None for _ in range(dimension)] for _ in range(dimension)]

    for edge in edges:
        mat[edge[0] - 1][edge[1] - 1] = problem.get_weight(*edge)

    return mat

def convert(src, dst):
    problem = tsplib95.load(src)
    mat = get_matrix(problem)
    f = open(dst, "w")
    f.write(str(len(mat)) + ' ')
    for row in mat:
        for el in row:
            f.write(str(el) + ' ')
    f.close()

if __name__ == '__main__':
    src = sys.argv[1]
    dst = sys.argv[2]

    convert(src, dst)