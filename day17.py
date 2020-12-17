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



raw_data = open('day17.txt','r').readlines()
ndim = 3
on = make(raw_data, ndim)
for _ in range(6):
    on = iter(on, ndim)
print(len(on))

ndim = 4
on = make(raw_data, ndim)
for _ in range(6):
    on = iter(on, ndim)
print(len(on))