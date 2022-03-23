import tsplib95
import numpy as np
import time


def nearest_neighbour(problem, vertex=0):
    if vertex < 0 or vertex > len(list(problem.get_nodes())):
        return
    
    visited = [False for _ in problem.get_nodes()]
    visited[vertex] = True

    tour = []
    tour.append(vertex)

    while False in visited:
        cost = np.inf
        nextVertex = int
        for i in problem.get_nodes():
            if vertex == i or visited[i]:
                continue
            curCost = problem.get_weight(*(vertex, i))
            if cost > curCost:
                cost = curCost
                nextVertex = i

        tour.append(nextVertex)
        vertex = nextVertex
        visited[vertex] = True

    problem.tours.append(tour)
    return tour


def get_resuts(problem, vertex=1):
    start = time.time_ns()
    tour = nearest_neighbour(problem, vertex)
    runtime = time.time_ns() - start

    return (problem.trace_tours([tour])[0], runtime)

if __name__ == '__main__':
    problem = tsplib95.load('../data/br17.atsp')
    print(get_resuts(problem, 1))

