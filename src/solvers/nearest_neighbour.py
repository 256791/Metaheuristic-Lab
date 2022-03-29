from ctypes import *
import tsplib95
import numpy as np
import time

# def nearest_neighbour(problem, vertex=0):
#     if vertex < 0 or vertex > len(list(problem.get_nodes())):
#         return
    
#     visited = [False for _ in problem.get_nodes()]
#     visited[vertex] = True

#     tour = []
#     tour.append(vertex)

#     while False in visited:
#         cost = np.inf
#         nextVertex = int
#         for i in problem.get_nodes():
#             if vertex == i or visited[i]:
#                 continue
#             curCost = problem.get_weight(*(vertex, i))
#             if cost > curCost:
#                 cost = curCost
#                 nextVertex = i

#         tour.append(nextVertex)
#         vertex = nextVertex
#         visited[vertex] = True

#     problem.tours.append(tour)
#     return tour
x = None
if __name__ == '__main__':
    x = cdll.LoadLibrary('./nearest_neighbour_cpp/nearest_neighbour.so')
else:
    x = cdll.LoadLibrary('./solvers/nearest_neighbour_cpp/nearest_neighbour.so')


x.nearest_neighbour.argtypes = [POINTER(POINTER(c_double)), c_int, c_int]
x.nearest_neighbour.restype = POINTER(c_int)

def get_full_matrix(problem):
    mat = []
    for i in problem.get_nodes():
        arr = []
        for j in problem.get_nodes():
            arr.append(problem.get_weight(i,j))
        mat.append(arr)
    return mat

def c_double_mat(mat):
    arr = []
    for i in range(len(mat)):
        arr.append((c_double * len(mat))(*mat[i]))
    return (POINTER(c_double) * len(mat))(*arr)
    
def nearest_neighbour(problem, vertex=0):
    if vertex < 0 or vertex > len(list(problem.get_nodes())):
        return
    
    mat = get_full_matrix(problem)

    c_path = x.nearest_neighbour(c_double_mat(mat), c_int(len(mat)), c_int(vertex))
    
    path = []
    nodes = list(problem.get_nodes())
    for i in range(len(mat)):
        path.append(nodes[c_path[i]])

    problem.tours.append(path)
    return path


def get_resuts(problem, vertex=1):
    start = time.time_ns()
    tour = nearest_neighbour(problem, vertex)
    runtime = time.time_ns() - start

    return (problem.trace_tours([tour])[0], runtime)

if __name__ == '__main__':
    problem = tsplib95.load('../data/br17.atsp')
    print(get_resuts(problem, 1))

