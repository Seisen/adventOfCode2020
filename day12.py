with open("day12.txt") as f:
    inputs = f.read()
    inputs = inputs.splitlines()
######################
########PART1#########
######################

def add_angle(angle: int, turn: int) -> int:
    res = angle + turn
    if res >= 360:
        res -= 360
    elif res<0:
        res += 360
    return res

def get_distance() -> int:
    N, E, S, W, DIR = 0, 0, 0, 0, 90
    moveF = {
        0: lambda x, y: (x, 0, 0, 0, y),
        90: lambda x, y: (0, x, 0, 0, y),
        180: lambda x, y: (0, 0, x, 0, y),
        270: lambda x, y: (0, 0, 0, x, y)
    }

    Actions = {
        'N': lambda x, y: (x, 0, 0, 0, y),
        'S': lambda x, y: (0, 0, x, 0, y),
        'E': lambda x, y: (0, x, 0, 0, y),
        'W': lambda x, y: (0, 0, 0, x, y),
        'F': lambda x, y: moveF[y](x, y),
        'R': lambda x, y: (0, 0, 0, 0, add_angle(y, x)),
        'L': lambda x, y: (0, 0, 0, 0, add_angle(y, -x))
    }
    for input in inputs:

        Ntemp, Etemp, Stemp, Wtemp, DIRtemp = Actions[input[0]](int(input[1:]), DIR)
        N += Ntemp
        E += Etemp
        S += Stemp
        W += Wtemp
        DIR = DIRtemp

    return abs(S-N)+abs(W-E)
print(get_distance())