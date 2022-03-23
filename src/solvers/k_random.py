import tsplib95
import numpy as np
import time

def k_random(problem, k=1):
    if k < 1:
        return
    cost = np.inf
    tour = []
    for _ in range(k):
        curTour = list(problem.get_nodes())
        np.random.shuffle(curTour)
        curCost = problem.trace_tours([curTour])[0]
        if cost > curCost:
            cost = curCost
            tour = curTour

    problem.tours.append(tour)
    return tour


def get_resuts(problem, k=1):
    start = time.time_ns()
    tour = k_random(problem, k)
    runtime = time.time_ns() - start

    return (problem.trace_tours([tour])[0], runtime)

if __name__ == '__main__':
    problem = tsplib95.load('../data/br17.atsp')
    print(get_resuts(problem, 10))
