from collections import Counter

with open('day10.txt') as f:
    inputs = f.read()
inputs = sorted(list(map(int, inputs.splitlines())))


def func(inputs: list):
    one_jolt, three_jolt = 0, 0

    while len(inputs) != 1:
        elem = inputs[0]
        inputs.pop(0)
        if inputs[0]-elem == 1:
            one_jolt += 1
        else:
            three_jolt += 1
    print((one_jolt+1)*(three_jolt+1))




def find_combinations(adapters):

    adapters.append(adapters[-1] + 3)
    counter = Counter()
    counter[0] = 1
    for adapter in adapters:
        counter[adapter] = counter[adapter - 1] + counter[adapter - 2] + counter[adapter - 3]
    print(counter[adapters[-1]])
