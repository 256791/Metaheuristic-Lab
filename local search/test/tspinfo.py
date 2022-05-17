import csv
import pprint
import sys
import re
from os import listdir
from os.path import isfile, join


def getTSPList(dir):
    files = [dir+f for f in listdir(dir) if isfile(join(dir, f))]
    tspfiles = list(filter(lambda f: f.endswith('tsp'), files))
    return tspfiles


def getSolutions(filename):
    try:
        with open(filename, newline='') as f:
            reader = csv.reader(f)
            return list(reader)
    except:
        return []


def getTSPInfo(dir):
    instances = []
    solutions = getSolutions(dir+'solutions.atsp.csv') + \
        getSolutions(dir+'solutions.tsp.csv')
    for file in getTSPList(dir+'atsp/') + getTSPList(dir+'tsp/'):
        filename = file.split('/')[-1]
        name = filename.split('.')[0]
        size = int(re.search(r"[0-9]+", name).group())
        filetype = filename.split('.')[1]
        solution = next((int(e[1]) for e in solutions if e[0] == name), None)
        
        instances.append({'name': name, 'file': file, 'size': size,
                        'solution': solution, 'type': filetype})

    instances = sorted(instances, key = lambda x: x['size'])
    return instances


if __name__ == '__main__':
    pp = pprint.PrettyPrinter(depth=6, width=200)
    pp.pprint(getTSPInfo(sys.argv[1]))
