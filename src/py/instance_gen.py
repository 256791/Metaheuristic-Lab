from enum import Enum
import numpy as np

class InstanceType(Enum):
    SYMETRIC = 1
    ASYMETRIC = 2
    EUC2D = 3

def header(name, filetype, comment, dimension, edgeWeightType):
    return "NAME: " + filename + "\n" +
            "TYPE: " + filetype + "\n" +
            "COMMENT: " + description + "\n" +
            "DIMENSION: " + dimension + "\n" +
            "EDGE_WEIGHT_TYPE: " + edgeWeightType + "\n"

def to_atsp(filename, mat, dimension, description, maxVal):
    f = open(filename + ".atsp", "w")
    f.write(header(filename, "ATSP", description, dimension, "EXPLICIT"))
    f.write("EDGE_WEIGHT_FORMAT: FULL_MATRIX\n")
    f.write("EDGE_WEIGHT_SECTION\n")

    maxLen = len(str(maxVal)) + 1

    for y in mat:
        for x in y:
            curLen = len(str(x))
            f.write(" " * (maxLen - curLen))
            f.write(x)
        f.write("\n")

    f.write(" " + maxVal + "\n")
    f.write("EOF\n")
    f.close()
    return None

def to_tsp(filename, coords, dimension, description, maxVal):
    f = open(filename + ".tsp", "w")
    f.write(header(filename, "TSP", description, dimension, "EUC_2D"))
    f.write("NODE_COORD_SECTION\n")

    maxLen = len(str(maxVal)) + 1

    for i in range(dimension):
        f.write(i + " " + coords[i][0] + " " + coords[i][1] + "\n")

    f.write("EOF\n")
    f.close()
    return None

def gen_random_instance(filename, dimension, instanceType=InstanceType.SYMETRIC, description="none", minVal = 0, maxVal = 50):
    if(instanceType == InstanceType.EUC2D):
        mat = np.random.random_integers(minVal, maxVal, (dimension, 2))
        to_tsp(filename, mat, dimension, description, maxVal)
        return mat

    mat = np.random.random_integers(minVal, maxVal, (dimension, dimension))
    for i in range(0,dimension):
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
        