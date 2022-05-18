import pandas as pd
import matplotlib.pyplot as plt


def plot(filename, axis, title, out, merge=False):
    plt.clf()
    plt.title(title)
    df = pd.read_csv(filename)

    x = df['instance_name']
    if merge:
        df = df.groupby('instance_size')[axis].mean()
        df.reset_index(inplace=True)
        x = df['instance_size']
        plt.xticks(df['instance_size'])

    for ax in axis:
        plt.plot(x, df[ax],  label=ax)

    plt.legend()
    if not merge:
        plt.xticks(rotation=90)
    plt.savefig(out)


plt.figure(figsize=(16, 8))

# TSPLib

plot('../data/tests/timePrd.csv', ['invert_time', 'swap_time', 'insert_time'], 'Time to instance', '../data/plots/time.png', False)
plot('../data/tests/timePrd.csv', ['invert_prd', 'swap_prd', 'insert_prd'], 'PRD to instance', '../data/plots/prd.png', False)

plot('../data/tests/tabuSize_invert.csv', ['sqrt_n_prd', 'log2_n_prd', 'n/2_prd', 'n_prd'], 'Invert PRD to instance for tabu function', '../data/plots/tabu_inv_prd.png', False)
plot('../data/tests/tabuSize_insert.csv', ['sqrt_n_prd', 'log2_n_prd', 'n/2_prd', 'n_prd'], 'Insert PRD to instance for tabu function', '../data/plots/tabu_ins_prd.png', False)
plot('../data/tests/tabuSize_swap.csv', ['sqrt_n_prd', 'log2_n_prd', 'n/2_prd', 'n_prd'], 'Swap PRD to instance for tabu function', '../data/plots/tabu_swp_prd.png', False)

plot('../data/tests/tabuSize_invert.csv', ['sqrt_n_time', 'log2_n_time', 'n/2_time', 'n_time'], 'Invert time to instance for tabu function', '../data/plots/tabu_inv_time.png', False)
plot('../data/tests/tabuSize_insert.csv', ['sqrt_n_time', 'log2_n_time', 'n/2_time', 'n_time'], 'Insert time to instance for tabu function', '../data/plots/tabu_ins_time.png', False)
plot('../data/tests/tabuSize_swap.csv', ['sqrt_n_time', 'log2_n_time', 'n/2_time', 'n_time'], 'Swap time to instance for tabu function', '../data/plots/tabu_swp_time.png', False)


plot('../data/tests/maxDepth_invert.csv', ['sqrt_n_prd', 'log2_n_prd', 'n/2_prd', 'n_prd'], 'Invert PRD to instance for max depth function', '../data/plots/depth_inv_prd.png', False)
plot('../data/tests/maxDepth_insert.csv', ['sqrt_n_prd', 'log2_n_prd', 'n/2_prd', 'n_prd'], 'Insert PRD to instance for max depth function', '../data/plots/depth_ins_prd.png', False)
plot('../data/tests/maxDepth_swap.csv', ['sqrt_n_prd', 'log2_n_prd', 'n/2_prd', 'n_prd'], 'Swap PRD to instance for max depth function', '../data/plots/depth_swp_prd.png', False)

plot('../data/tests/maxImpiter_invert.csv', ['pow2_n_prd', '2_pow2_n_prd', '100n_prd', 'log_n_pow2_n_prd'], 'Invert PRD to instance for max iter without improvement function', '../data/plots/impiter_inv_prd.png', False)
plot('../data/tests/maxImpiter_insert.csv', ['pow2_n_prd', '2_pow2_n_prd', '100n_prd', 'log_n_pow2_n_prd'], 'Insert PRD to instance for max iter without improvement function', '../data/plots/impiter_ins_prd.png', False)
plot('../data/tests/maxImpiter_swap.csv', ['pow2_n_prd', '2_pow2_n_prd', '100n_prd', 'log_n_pow2_n_prd'], 'Swap PRD to instance for max iter without improvement function', '../data/plots/impiter_swp_prd.png', False)


# Random

plot('../data/tests/random/timePrd.csv', ['invert_time', 'swap_time', 'insert_time'], 'Avg Time to instance size', '../data/plots/rand_time.png', True)
plot('../data/tests/random/timePrd.csv', ['invert_prd', 'swap_prd', 'insert_prd'], 'Avg PRD to instance size', '../data/plots/rand_prd.png', True)

plot('../data/tests/random/tabuSize_invert.csv', ['sqrt_n_prd', 'log2_n_prd', 'n/2_prd', 'n_prd'], 'Invert avg PRD to instance size for tabu function', '../data/plots/rand_tabu_inv_prd.png', True)
plot('../data/tests/random/tabuSize_insert.csv', ['sqrt_n_prd', 'log2_n_prd', 'n/2_prd', 'n_prd'], 'Insert avg PRD to instance size for tabu function', '../data/plots/rand_tabu_ins_prd.png', True)
plot('../data/tests/random/tabuSize_swap.csv', ['sqrt_n_prd', 'log2_n_prd', 'n/2_prd', 'n_prd'], 'Swap avg PRD to instance size for tabu function', '../data/plots/rand_tabu_swp_prd.png', True)

plot('../data/tests/random/tabuSize_invert.csv', ['sqrt_n_time', 'log2_n_time', 'n/2_time', 'n_time'], 'Invert avg time to instance size for tabu function', '../data/plots/rand_tabu_inv_time.png', True)
plot('../data/tests/random/tabuSize_insert.csv', ['sqrt_n_time', 'log2_n_time', 'n/2_time', 'n_time'], 'Insert avg time to instance size for tabu function', '../data/plots/rand_tabu_ins_time.png', True)
plot('../data/tests/random/tabuSize_swap.csv', ['sqrt_n_time', 'log2_n_time', 'n/2_time', 'n_time'], 'Swap avg time to instance size for tabu function', '../data/plots/rand_tabu_swp_time.png', True)


plot('../data/tests/random/maxDepth_invert.csv', ['sqrt_n_prd', 'log2_n_prd', 'n/2_prd', 'n_prd'], 'Invert avg PRD to instance size for max depth function', '../data/plots/rand_depth_inv_prd.png', True)
plot('../data/tests/random/maxDepth_insert.csv', ['sqrt_n_prd', 'log2_n_prd', 'n/2_prd', 'n_prd'], 'Insert avg PRD to instance size for max depth function', '../data/plots/rand_depth_ins_prd.png', True)
plot('../data/tests/random/maxDepth_swap.csv', ['sqrt_n_prd', 'log2_n_prd', 'n/2_prd', 'n_prd'], 'Swap avg PRD to instance size for max depth function', '../data/plots/rand_depth_swp_prd.png', True)

plot('../data/tests/random/maxImpiter_invert.csv', ['pow2_n_prd', '2_pow2_n_prd', '100n_prd', 'log_n_pow2_n_prd'], 'Invert avg PRD to instance size for max iter without improvement function', '../data/plots/rand_impiter_inv_prd.png', True)
plot('../data/tests/random/maxImpiter_insert.csv', ['pow2_n_prd', '2_pow2_n_prd', '100n_prd', 'log_n_pow2_n_prd'], 'Insert avg PRD to instance size for max iter without improvement function', '../data/plots/rand_impiter_ins_prd.png', True)
plot('../data/tests/random/maxImpiter_swap.csv', ['pow2_n_prd', '2_pow2_n_prd', '100n_prd', 'log_n_pow2_n_prd'], 'Swap avg PRD to instance size for max iter without improvement function', '../data/plots/rand_impiter_swp_prd.png', True)