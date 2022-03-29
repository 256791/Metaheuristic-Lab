import matplotlib.pyplot as plt
import tsplib95 as tsp
from solvers import nearest_neighbour, k_random, two_opt
from tsp_tools import InstanceType, gen_random_instance


def prepare_tests(sizes, type):
    tests = []
    for s in sizes:
        if type == InstanceType.ASYMETRIC:
            gen_random_instance('tests/a_' + str(s), s, InstanceType.ASYMETRIC)
            tests.append(tsp.load(f'./data/tests/a_{s}.atsp'))
        elif type == InstanceType.EUC2D:
            gen_random_instance('tests/e_' + str(s), s, InstanceType.EUC2D)
            tests.append(tsp.load(f'./data/tests/e_{s}.tsp'))
        elif type == InstanceType.SYMETRIC:
            gen_random_instance('tests/s_' + str(s), s, InstanceType.SYMETRIC)
            tests.append(tsp.load(f'./data/tests/s_{s}.atsp'))

    return tests


def plot_test(namesufix, axis, col, sizes, times, prds, labels):
    axis[0, col].set_title("Avg path" + namesufix)
    axis[1, col].set_title("Avg PRD" + namesufix)
    axis[2, col].set_title("Avg Time" + namesufix)

    for i in range(len(labels)):
        axis[0, col].plot(sizes, prds[i], label=labels[i])
        axis[2, col].plot(sizes, times[i], label=labels[i])

    axis[0, col].legend(loc="upper right")
    axis[1, col].legend(loc="upper right")
    axis[2, col].legend(loc="upper right")
    
    


def run_tests(instances, algorithm, repeat=1):
    path = []
    time = []

    for instance in instances:
        time.append(0)
        path.append(0)
        for ignore in range(0, repeat):
            p, t = algorithm(instance)

            path[-1] += p
            time[-1] += t

        path[-1] /= repeat
        time[-1] /= repeat
    return (path, time)


def test(sizes):
    figure, axis = plt.subplots(3, 3)
    figure.set_figheight(16.2)
    figure.set_figwidth(19.2)

    asym_t = prepare_tests(sizes, InstanceType.ASYMETRIC)
    sym_t = prepare_tests(sizes, InstanceType.SYMETRIC)
    euc_t = prepare_tests(sizes, InstanceType.EUC2D)

    labels = ['nearest_neighbour', 'k_random', 'two_opt']

    asym_path = []
    asym_time = []
    sym_path = []
    sym_time = []
    euc_path = []
    euc_time = []
    

    p,t = run_tests(asym_t, nearest_neighbour.get_resuts)
    asym_path.append(p)
    asym_time.append(t)
    p,t = run_tests(asym_t, k_random.get_resuts)
    asym_path.append(p)
    asym_time.append(t)
    p,t = run_tests(asym_t, two_opt.get_results)
    asym_path.append(p)
    asym_time.append(t)

    plot_test(' asymetric', axis, 0, sizes, asym_time, asym_path, labels)


    p,t = run_tests(sym_t, nearest_neighbour.get_resuts)
    sym_path.append(p)
    sym_time.append(t)
    p,t = run_tests(sym_t, k_random.get_resuts)
    sym_path.append(p)
    sym_time.append(t)
    p,t = run_tests(sym_t, two_opt.get_results)
    sym_path.append(p)
    sym_time.append(t)

    plot_test(' symetric', axis, 1, sizes, sym_time, sym_path, labels)


    # labels = [ 'k_random', 'two_opt']
    p,t = run_tests(euc_t, nearest_neighbour.get_resuts)
    euc_path.append(p)
    euc_time.append(t)
    
    p,t = run_tests(euc_t, k_random.get_resuts)
    euc_path.append(p)
    euc_time.append(t)
    p,t = run_tests(euc_t, two_opt.get_results)
    euc_path.append(p)
    euc_time.append(t)

    plot_test(' euclidean2D', axis, 2, sizes, euc_time, euc_path, labels)

    

    # plt.show()
    plt.savefig('fig.png')


if __name__ == '__main__':
    test(range(10, 100, 10))
