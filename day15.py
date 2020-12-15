with open("day15.txt") as f:
    inputs = [int(x) for x in f.read().split(',')]


def part1(inputs, stop: int = 2020) -> int:
    """

    :param inputs:list of inputs
    :param stop: when to stop
    :return: last value
    """

    values = {value: index for index, value in enumerate(inputs[:-1])}
    current = inputs[-1]
    for turn in range(len(values), stop - 1):
        last = current
        current = turn - values.get(current, turn)
        values[last] = turn
    return current

print(part1(inputs))
print(part1(inputs, 30000000))