from itertools import combinations

with open('day9.txt') as f:
    inputs = f.read()
inputs = list(map(int, inputs.splitlines()))


def first_not_valid(previous_numbers: int):
    i = iter(inputs)
    l: list = [next(i) for x in range(previous_numbers+1)]
    valid: bool = True

    while valid:

        del l[0]
        l.append(next(i))
        valid = False

        for elem in combinations(l[:-1], 2):
            if sum(elem) == l[-1]:
                valid = True
                break

    return l[-1]


def weakness(error):
    items = []
    for item in inputs:
        if item > error:
            return
        items.append(item)
        while sum(items) > error:
            items.pop(0)
        if sum(items) == error:
            return min(items) + max(items)

print(first_not_valid(25))
print(weakness(first_not_valid(25)))
