import subprocess
import time
from tspinfo import getTSPInfo 
from math import floor, sqrt

TABU_PATH = '"C:/Users/algod/Desktop/Algorytmy Metaheurystyczne/Metaheuristic-Lab/local search/tabu"'


def tsp(input, max_imp_iter=100, max_depth=100, max_tabu=5, mode="invert", max_iter=1000, threads=4, clear_tabu=False, debug=False):

    t = int(time.time() * 1000)
    args = ['../tabu', '-input', input, "-max_iter", str(max_iter), "-max_depth", str(max_depth), 
        '-max_imp_iter', str(max_imp_iter), "-max_tabu", str(max_tabu), "-threads", str(threads), "-mode", str(mode)]
    if clear_tabu:
        args.append('-clear_tabu')
        
    if debug:
        args.append('-print_debug')

    res = subprocess.run(args, capture_output=True)
    t = int(time.time() * 1000) - t

    if res.stderr.decode('utf-8') != '':
        print('Error')
        return None

    data = res.stdout.decode('utf-8').split('\n')[:-1]
    if(debug):
        tour = [int(i) for i in data[-2].split(' ')[:-1]]
        cost = int(data[-1])
        return (t, tour, cost, res.stdout.decode('utf-8'))
    else:
        tour = [int(i) for i in data[0].split(' ')[:-1]]
        cost = int(data[1])
        return (t, tour, cost)


if __name__  == '__main__':
    instances = getTSPInfo('../data/tsplib/')
    print('Avaliable instances: ')
    for el in instances:
        print(el['name'])

    name = input('\nEnter instance name: ')

    instance = next((i for i in instances if i['name']==name), [None])
    if instance == None:
        print('No instance named ' + name + ' found')
    else:
        n = instance['size']
        instance['matfile'] = f'../data/tspmat/{instance["name"]}.mat'
        result = tsp(instance['matfile'], n*n*2, floor(sqrt(n)), floor(sqrt(n)), 'insert', 100000, 8, True, True)
        print(result[3])
        print(result[0])
        print(f'\ncost: {result[2]} opt: {instance["solution"]} prd: {100*(result[2]- instance["solution"])/instance["solution"]}')
