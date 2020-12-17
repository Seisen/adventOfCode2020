<<<<<<< HEAD
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
=======
with open("day17.txt") as f:
    inputs = f.read().splitlines()


def initial_state(z: int = 0, cubes: list = []) -> list:
    """

    :param z: position z
    :param cubes: list of active cubes
    :return: cubes
    """
    for y, input in enumerate(inputs):
        for x, cube in enumerate(input):
            if cube == "#":
                cubes.append([x, y, z])
    return cubes


def find_max(dim: int, cubes: list) -> int:
    """

    :param dim: (x,y,z) -> (0,1,2)
    :param cubes: list of active cuves
    :return: max for a dim
    """
    try:
        return max([cube[dim] for cube in cubes])+1

    except IndexError:
        assert "Range is 0-3"


def check_neighbors(x, y, z, cubes, cpt: int = 0) -> int:
    """

    :param x: coo x of the cube
    :param y: coo y of the cube
    :param z: coo z of the cube
    :param cubes: list of active cubes
    :param cpt: counter of active neighbors
    :return: cpt
    """

    for n_x in range(x-1, x+2):
        for n_y in range(y-1, y+2):
            for n_z in range(z - 1, z + 2):
                if n_x != x or n_y != y or n_z != z:
                    if [n_x, n_y, n_z] in cubes:
                        cpt += 1
    return cpt


def boot_process(cycle: int = 0, cyles: int = 6, cubes: list = initial_state()):
    """

    :param cycle: num of the current index
    :param cyles: max of cycles
    :param cubes: list of active cubes
    :return: len of cubes
    """
    if cycle <= cyles:
        x_max, y_max, z_max = find_max(0, cubes), find_max(1, cubes), find_max(2, cubes)
        for x in range(-x_max, x_max):
            for y in range(-y_max, y_max):
                for z in range(-z_max, z_max):
                    cpt_active_neighbor = check_neighbors(x, y, z, cubes)

                    if ([x, y, z] in cubes):
                        if cpt_active_neighbor == 2 or cpt_active_neighbor == 3:
                            cubes.remove([x, y, z])


                    elif cpt_active_neighbor == 3:
                        cubes.append([x, y, z])

        #cubes = [[x + 1, y + 1, z + 1] for x, y, z in cubes]
        boot_process(cycle+1, cyles, cubes)

    else:
        print(len(cubes))
boot_process()
>>>>>>> 5fa34609b6838bb6f1a9cdd62301408ff8430d93
