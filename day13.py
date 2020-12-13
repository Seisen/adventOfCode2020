from itertools import filterfalse

#parameters
with open("day13.txt") as f:
    inputs = f.read()
    inputs = inputs.splitlines()
    time_stamp = int(inputs[0])
    bus_ids = [int(x) for x in filterfalse(lambda y:y == "x", inputs[1].split(','))]
    func = lambda x: x != "x" and int(x) or x
    bus_ids2= [func(x) for x in inputs[1].split((','))]

#####################################
#############PART 1##################
#####################################

def next_time_stamp(time_stamp: int,bus_id : int) -> int:
    if time_stamp % bus_id == 0:
        return time_stamp
    else:
        return next_time_stamp(time_stamp+1, bus_id)


def earliest_bus() -> int:
    time_next_bus: list = [next_time_stamp(time_stamp, bus_id) for bus_id in bus_ids]

    return bus_ids[time_next_bus.index(min(time_next_bus))]*(min(time_next_bus)-time_stamp)

#####################################
#############PART 2##################
#####################################

def matching_step(t1: int, t2: int,gap: int,cpt: int = 1) -> int:

    if ((t1 * cpt) + gap) % t2 == 0:
        return (t1 * cpt)
    else:
        return matching_step(t1, t2, gap, cpt+1)



def matching_list_position() -> int:

    buses = [x for x in bus_ids2 if type(x) is int]
    mods = [-i % v for i, v in enumerate(bus_ids2) if v != 'x']
    x, step = 0, 1
    for d, r in zip(buses, mods):

        while x % d != r:
            x += step
        step *= d
    return x

print(matching_list_position())