import pandas as pd
from math import sqrt, ceil, floor, log2, log
from tsp import tsp


def test(instances, max_imp_lmbd=lambda x: 2*x['size']*x['size'], max_depth_lmbd=lambda x: floor(sqrt(x['size'])), max_tabu_lmbd=lambda x: floor(sqrt(x['size'])), max_iter=50000):
    results = []
    for i in instances:
        print(i['name'])
        time_inv, tour_inv, cost_inv = tsp(i['matfile'], max_imp_lmbd(
            i), max_depth_lmbd(i), max_tabu_lmbd(i), 'invert', 50000, 8, True)
        time_ins, tour_ins, cost_ins = tsp(i['matfile'], max_imp_lmbd(
            i), max_depth_lmbd(i), max_tabu_lmbd(i), 'insert', 50000, 8, True)
        time_swp, tour_swp, cost_swp = tsp(i['matfile'], max_imp_lmbd(
            i), max_depth_lmbd(i), max_tabu_lmbd(i), 'swap', 50000, 8, True)

        opt = min([cost_inv, cost_ins, cost_swp])
        if 'solution' in i:
            if i['solution'] != None:
                opt = int(i['solution'])

        prd_inv = 100 * (cost_inv - opt) / opt
        prd_ins = 100 * (cost_ins - opt) / opt
        prd_swp = 100 * (cost_swp - opt) / opt

        results.append((i['size'], i['name'], (time_inv, prd_inv),
                       (time_ins, prd_ins), (time_swp, prd_swp)))

    return results


def testTabuSize(instances, filename):
    df_inv = pd.DataFrame(columns=['instance_size', 'instance_name', 'sqrt_n_time',
                                   'log2_n_time', 'n/2_time', 'n_time', 'sqrt_n_prd',
                                   'log2_n_prd', 'n/2_prd', 'n_prd'])
    df_ins = pd.DataFrame(columns=['instance_size', 'instance_name', 'sqrt_n_time',
                                   'log2_n_time', 'n/2_time', 'n_time', 'sqrt_n_prd',
                                   'log2_n_prd', 'n/2_prd', 'n_prd'])
    df_swp = pd.DataFrame(columns=['instance_size', 'instance_name', 'sqrt_n_time',
                                   'log2_n_time', 'n/2_time', 'n_time', 'sqrt_n_prd',
                                   'log2_n_prd', 'n/2_prd', 'n_prd'])

    r_sqrt = test(instances, max_tabu_lmbd=lambda x: floor(sqrt(x['size'])))
    r_log2 = test(instances, max_tabu_lmbd=lambda x: floor(log2(x['size'])))
    r_div2 = test(instances, max_tabu_lmbd=lambda x: floor(x['size']/2))
    r_size = test(instances, max_tabu_lmbd=lambda x: x['size'])

    for i in range(len(r_sqrt)):
        df_inv.index = df_inv.index + 1
        df_inv.loc[-1] = [r_sqrt[i][0], r_sqrt[i][1], r_sqrt[i][2][0], r_log2[i][2][0],
                          r_div2[i][2][0], r_size[i][2][0], r_sqrt[i][2][1], r_log2[i][2][1], r_div2[i][2][1], r_size[i][2][1]]

    for i in range(len(r_sqrt)):
        df_ins.index = df_ins.index + 1
        df_ins.loc[-1] = [r_sqrt[i][0], r_sqrt[i][1], r_sqrt[i][3][0], r_log2[i][3][0],
                          r_div2[i][3][0], r_size[i][3][0], r_sqrt[i][3][1], r_log2[i][3][1], r_div2[i][3][1], r_size[i][3][1]]

    for i in range(len(r_sqrt)):
        df_swp.index = df_swp.index + 1
        df_swp.loc[-1] = [r_sqrt[i][0], r_sqrt[i][1], r_sqrt[i][4][0], r_log2[i][4][0],
                          r_div2[i][4][0], r_size[i][4][0], r_sqrt[i][4][1], r_log2[i][4][1], r_div2[i][4][1], r_size[i][4][1]]

    df_inv.to_csv(filename + '_invert.csv', index=False)
    df_ins.to_csv(filename + '_insert.csv', index=False)
    df_swp.to_csv(filename + '_swap.csv', index=False)


def testMaxDepth(instances, filename):
    df_inv = pd.DataFrame(columns=['instance_size', 'instance_name', 'sqrt_n_time',
                                   'log2_n_time', 'n/2_time', 'n_time', 'sqrt_n_prd',
                                   'log2_n_prd', 'n/2_prd', 'n_prd'])
    df_ins = pd.DataFrame(columns=['instance_size', 'instance_name', 'sqrt_n_time',
                                   'log2_n_time', 'n/2_time', 'n_time', 'sqrt_n_prd',
                                   'log2_n_prd', 'n/2_prd', 'n_prd'])
    df_swp = pd.DataFrame(columns=['instance_size', 'instance_name', 'sqrt_n_time',
                                   'log2_n_time', 'n/2_time', 'n_time', 'sqrt_n_prd',
                                   'log2_n_prd', 'n/2_prd', 'n_prd'])

    r_sqrt = test(instances, max_depth_lmbd=lambda x: floor(sqrt(x['size'])))
    r_log2 = test(instances, max_depth_lmbd=lambda x: floor(log2(x['size'])))
    r_div2 = test(instances, max_depth_lmbd=lambda x: floor(x['size']/2))
    r_size = test(instances, max_depth_lmbd=lambda x: x['size'])

    for i in range(len(r_sqrt)):
        df_inv.index = df_inv.index + 1
        df_inv.loc[-1] = [r_sqrt[i][0], r_sqrt[i][1], r_sqrt[i][2][0], r_log2[i][2][0],
                          r_div2[i][2][0], r_size[i][2][0], r_sqrt[i][2][1], r_log2[i][2][1], r_div2[i][2][1], r_size[i][2][1]]

    for i in range(len(r_sqrt)):
        df_ins.index = df_ins.index + 1
        df_ins.loc[-1] = [r_sqrt[i][0], r_sqrt[i][1], r_sqrt[i][3][0], r_log2[i][3][0],
                          r_div2[i][3][0], r_size[i][3][0], r_sqrt[i][3][1], r_log2[i][3][1], r_div2[i][3][1], r_size[i][3][1]]

    for i in range(len(r_sqrt)):
        df_swp.index = df_swp.index + 1
        df_swp.loc[-1] = [r_sqrt[i][0], r_sqrt[i][1], r_sqrt[i][4][0], r_log2[i][4][0],
                          r_div2[i][4][0], r_size[i][4][0], r_sqrt[i][4][1], r_log2[i][4][1], r_div2[i][4][1], r_size[i][4][1]]

    df_inv.to_csv(filename + '_invert.csv', index=False)
    df_ins.to_csv(filename + '_insert.csv', index=False)
    df_swp.to_csv(filename + '_swap.csv', index=False)


def testMaxImpiter(instances, filename):
    df_inv = pd.DataFrame(columns=['instance_size', 'instance_name', 'pow2_n_time',
                                   '2_pow2_n_time', '100n_time', 'log_n_pow2_n_time', 'pow2_n_prd',
                                   '2_pow2_n_prd', '100n_prd', 'log_n_pow2_n_prd'])
    df_ins = pd.DataFrame(columns=['instance_size', 'instance_name', 'pow2_n_time',
                                   '2_pow2_n_time', '100n_time', 'log_n_pow2_n_time', 'pow2_n_prd',
                                   '2_pow2_n_prd', '100n_prd', 'log_n_pow2_n_prd'])
    df_swp = pd.DataFrame(columns=['instance_size', 'instance_name', 'pow2_n_time',
                                   '2_pow2_n_time', '100n_time', 'log_n_pow2_n_time', 'pow2_n_prd',
                                   '2_pow2_n_prd', '100n_prd', 'log_n_pow2_n_prd'])

    r_pow2 = test(instances, max_imp_lmbd=lambda x: x['size']*x['size'])
    r_pow2mul2 = test(instances, max_imp_lmbd=lambda x: x['size']*x['size']*2)
    r_mul100 = test(instances, max_imp_lmbd=lambda x: x['size']*100)
    r_pow2mullog2 = test(
        instances, max_imp_lmbd=lambda x: x['size']*x['size']*ceil(log(x['size'])))

    for i in range(len(r_pow2)):
        df_inv.index = df_inv.index + 1
        df_inv.loc[-1] = [r_pow2[i][0], r_pow2[i][1], r_pow2[i][2][0], r_pow2mul2[i][2][0],
                          r_mul100[i][2][0], r_pow2mullog2[i][2][0], r_pow2[i][2][1], r_pow2mul2[i][2][1], r_mul100[i][2][1], r_pow2mullog2[i][2][1]]

    for i in range(len(r_pow2)):
        df_ins.index = df_ins.index + 1
        df_ins.loc[-1] = [r_pow2[i][0], r_pow2[i][1], r_pow2[i][3][0], r_pow2mul2[i][3][0],
                          r_mul100[i][3][0], r_pow2mullog2[i][3][0], r_pow2[i][3][1], r_pow2mul2[i][3][1], r_mul100[i][3][1], r_pow2mullog2[i][3][1]]

    for i in range(len(r_pow2)):
        df_swp.index = df_swp.index + 1
        df_swp.loc[-1] = [r_pow2[i][0], r_pow2[i][1], r_pow2[i][4][0], r_pow2mul2[i][4][0],
                          r_mul100[i][4][0], r_pow2mullog2[i][4][0], r_pow2[i][4][1], r_pow2mul2[i][4][1], r_mul100[i][4][1], r_pow2mullog2[i][4][1]]

    df_inv.to_csv(filename + '_invert.csv', index=False)
    df_ins.to_csv(filename + '_insert.csv', index=False)
    df_swp.to_csv(filename + '_swap.csv', index=False)


def testTimePrd(instances, filename):
    data = test(instances)
    df = pd.DataFrame(columns=['instance_size', 'instance_name', 'invert_time',
                      'insert_time', 'swap_time', 'invert_prd', 'insert_prd', 'swap_prd'])

    for row in data:
        df.index = df.index + 1
        df.loc[-1] = [row[0], row[1], row[2][0], row[3][0],
                      row[4][0], row[2][1], row[3][1], row[4][1]]

    df.to_csv(filename + '.csv', index=False)
