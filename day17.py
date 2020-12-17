from time import time
from collections import Counter
from itertools import product


def make(raw_data, ndim):
    on = set()
    for i, row in enumerate(raw_data):
        for j, val in enumerate(row):
            if val == '#':
                on.add(tuple([i,j] + [0] * (ndim-2)))
    return on

def iter(on, ndim):
    c = Counter()
    for loc in on:
        for delta in product([-1, 0, 1], repeat=ndim):
            new = tuple([a+b for a, b in zip(loc, delta)])
            if new != loc:
                c[new] += 1
    keep_on = set([loc for loc in on if c[loc] in [2,3]])
    turn_on = set([loc for loc, v in c.items() if loc not in on and v==3])
    return keep_on  | turn_on


def boot(ndim: int, cycles: int = 6):
    inputs = open('day17.txt', 'r').readlines()
    on = make(inputs, ndim)
    for _ in range(cycles):
        on = iter(on, ndim)
    print(len(on))


if __name__ == "__main__":
    t_start = time()
    boot(3)
    print("temps d'execution avec dim=3: "+str(time()-t_start))

    t_start = time()
    boot(4)
    print("temps d'execution avec dim=4: " + str(time() - t_start))

