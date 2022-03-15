from enum import Enum
import numpy as np

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
    f = open(f"../data/{filename}.atsp", "w")
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
    f = open(f"../data/{filename}.tsp", "w")
    f.write(header(filename, "TSP", description, dimension, "EUC_2D"))
    f.write("NODE_COORD_SECTION\n")

    for i in range(dimension):
        f.write(f"{i} {coords[i][0]}.0 {coords[i][1]}.0\n")

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
        

if __name__ == '__main__':
    gen_random_instance("test_symetric", 10, InstanceType.SYMETRIC)
    gen_random_instance("test_euc2d", 10, InstanceType.EUC2D)
    gen_random_instance("test_asymetric", 10, InstanceType.ASYMETRIC)
    