from ctypes import *
import tsplib95

# def two_opt_swap(tour, i, k):
#     swapped = tour[0:i]
#     rew = tour[i:k]
#     rew.reverse()
#     swapped += rew
#     swapped += tour[k:]
#     return swapped

# def two_opt_py(problem):
#     tour = list(problem.get_nodes())
#     ntour = tour
#     cost = problem.trace_tours([tour])[0]
#     ncost = cost
#     length = len(tour)

#     while True:
#         for i in range(0, length-1):
#             for k in range(i+1,length):
#                 nt = two_opt_swap(tour, i, k)
#                 ntc = problem.trace_tours([nt])[0]
#                 if ntc < ncost:
#                     ncost = ntc
#                     ntour = nt
#         if(ncost < cost):
#             tour = ntour
#             cost = ncost
#             # print(cost)
#         else:
#             break
#     problem.tours.append(tour)
#     return tour


x = cdll.LoadLibrary('./two_opt_cpp/two_opt.so')

x.two_opt.argtypes = [POINTER(POINTER(c_double)), c_int]
x.two_opt.restype = POINTER(c_int)

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

def two_opt(problem):
    
    mat = get_full_matrix(problem)

    c_path = x.two_opt(c_double_mat(mat), c_int(len(mat)))

    path = []
    nodes = list(problem.get_nodes())
    for i in range(len(mat)):
        path.append(nodes[c_path[i]])
    
    problem.tours.append(path)
    return path


if __name__ == '__main__':
    problem = tsplib95.load('../data/gr120.tsp')
    path = two_opt(problem)
    # path = two_opt_py(problem)
    print(path)
    print(problem.trace_tours([path])[0])