import math
import numpy as np
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
    f = open(f"{filename}", "w")
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
    f = open(f"{filename}", "w")
    f.write(header(filename, "TSP", description, dimension, "EUC_2D"))
    f.write("NODE_COORD_SECTION\n")

    for i in range(dimension):
        f.write(f"{i + 1} {coords[i][0]}.0 {coords[i][1]}.0\n")

    f.write("EOF\n")
    f.close()
    return None


def gen_random_instance(filename, dimension, instanceType=InstanceType.SYMETRIC, description="none", minVal=0, maxVal=50):
    if(instanceType == InstanceType.EUC2D):
        maxVal /= math.sqrt(2)
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


def genInstances(sizes, type, dir):
    # tests = []
    for s in sizes:
        if type == InstanceType.ASYMETRIC:
            gen_random_instance(f'{dir}/a_' + str(s) + '.atsp', s, InstanceType.ASYMETRIC)
            # tests.append(tsp.load(f'{dir}/a_{s}.atsp'))
        elif type == InstanceType.EUC2D:
            gen_random_instance(f'{dir}/e_' + str(s) + '.tsp', s, InstanceType.EUC2D)
            # tests.append(tsp.load(f'{dir}/e_{s}.tsp'))
        elif type == InstanceType.SYMETRIC:
            gen_random_instance(f'{dir}/s_' + str(s) + '.atsp', s, InstanceType.SYMETRIC)
            # tests.append(tsp.load(f'{dir}/s_{s}.atsp'))

    # return tests
