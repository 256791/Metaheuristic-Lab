from tspinfo import getTSPInfo
from tspgen import genInstances, InstanceType
from convert import convert
import tests as ts


def prepareRandInstances(rnge):
    genInstances(rnge, InstanceType.SYMETRIC, '../data/tsprand/tsp')
    genInstances(rnge, InstanceType.EUC2D, '../data/tsprand/tsp')
    genInstances(rnge, InstanceType.ASYMETRIC, '../data/tsprand/atsp')

    instances = getTSPInfo('../data/tsprand/')
    for el in instances:
        convert(el['file'], f'../data/tsprandmat/{el["name"]}.mat')

def prepareTSPInstances():
    instances = getTSPInfo('../data/tsplib/')
    for el in instances:
        if(el['size'] < 1000):
            convert(el['file'], f'../data/tspmat/{el["name"]}.mat')

if __name__ == '__main__':
    # prepareTSPInstances()
    # prepareRandInstances(range(10, 21, 10))

    instances = getTSPInfo('../data/tsprand/')
    for e in instances:
        e['matfile'] = f'../data/tsprandmat/{e["name"]}.mat'

    print('start:')

    ts.testTimePrd(instances, '../data/tests/random/timePrd')
    ts.testTabuSize(instances, '../data/tests/random/tabuSize')
    ts.testMaxDepth(instances, '../data/tests/random/maxDepth')
    ts.testMaxImpiter(instances, '../data/tests/random/maxImpiter')


    # instances = list(
    #     filter(lambda e: e['size'] <= 80, getTSPInfo('../data/tsplib/')))
    # for e in instances:
    #     print(e['name'])
    #     e['matfile'] = f'../data/tspmat/{e["name"]}.mat'

    # print('start:')

    # ts.testTimePrd(instances, '../data/tests/timePrd')
    # ts.testTabuSize(instances, '../data/tests/tabuSize')
    # ts.testMaxDepth(instances, '../data/tests/maxDepth')
    # ts.testMaxImpiter(instances, '../data/tests/maxImpiter')





    # i = next(e for e in instances if e['name'] == 'gr48')
    # i = next(e for e in instances if e['name'] == 'berlin52')
    # i = next(e for e in instances if e['name'] == 'eil76')
    # i = next(e for e in instances if e['name'] == 'ch150')

    # print(tsp(i['matfile'], i['size']*i['size']*2, floor(sqrt(i['size'])), floor(sqrt(i['size'])), 'invert', 50000, 8, True))
    # print(i['solution'])

