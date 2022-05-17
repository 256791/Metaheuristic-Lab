import subprocess
import time

from numpy import integer

TABU_PATH = '"C:/Users/algod/Desktop/Algorytmy Metaheurystyczne/Metaheuristic-Lab/local search/tabu"'


def tsp(input, max_imp_iter=100, max_depth=100, max_tabu=5, mode="invert", max_iter=1000, threads=4, clear_tabu=False):

    t = int(time.time() * 1000)
    args = ['../tabu', '-input', input, "-max_iter", str(max_iter), "-max_depth", str(max_depth), 
        '-max_imp_iter', str(max_imp_iter), "-max_tabu", str(max_tabu), "-threads", str(threads), "-mode", str(mode)]
    if clear_tabu:
        args.append('-clear_tabu')
    res = subprocess.run(args, capture_output=True)
    t = int(time.time() * 1000) - t

    if res.stderr.decode('utf-8') != '':
        print('Error')
        return None

    data = res.stdout.decode('utf-8').split('\n')[:-1]
    tour = [int(i) for i in data[0].split(' ')[:-1]]
    cost = int(data[1])
    return (t, tour, cost)
