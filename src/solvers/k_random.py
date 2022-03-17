import tsplib95
import numpy as np


def k_random(problem, k):
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


if __name__ == '__main__':
    problem = tsplib95.load('../data/br17.atsp')
    k_random(problem, 10)
