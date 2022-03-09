from enum import Enum
import numpy as np

class InstanceType(Enum):
    SYMETRIC = 1
    ASYMETRIC = 2
    EUC2D = 3

def to_atsp(filename, mat, dimension, description, maxVal):
    f = open(filename + ".atsp", "w")
    f.write("NAME: " + filename + "\n")
    f.write("TYPE: ATSP\n")
    f.write("COMMENT: " + description + "\n")
    f.write("DIMENSION: " + dimension + "\n")
    f.write("EDGE_WEIGHT_TYPE: EXPLICIT\n")
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
    f.write("NAME: " + filename + "\n")
    f.write("TYPE: TSP\n")
    f.write("COMMENT: " + description + "\n")
    f.write("DIMENSION: " + dimension + "\n")
    f.write("EDGE_WEIGHT_TYPE: EUC_2D\n")
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
        