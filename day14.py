import re
from itertools import product
with open('day14.txt') as f:
    inputs = f.read().splitlines()

def groupByMask(inputs, i: int = 0, mem: list =[[]]) -> list:
    for j, input in enumerate(inputs):
        if input[0:3] != 'mem' and j != 0:
            i += 1
            mem.append([])
        elif input[0:3] == 'mem':
            mem[i].append(input)
    return mem


masks = [x[7:] for x in inputs if x[0:4] == 'mask']
values = groupByMask(inputs)


def part1(memory: dict = {}):

    for i, mask in enumerate(masks):
        for value in values[i]:#good luck reading the line below
            memory[re.search('\[([^\)]+)\]', value).group(1)] = int("0b"+"".join([mask[j] if mask[j] != 'X' else bin(int(re.search('\=(.*)', value).group(1)[1:]))[2:].zfill(36)[j] for j in range(36)]),2)
    return sum(memory.values())

def part2(memory: dict = {}):
    for i, mask in enumerate(masks):
        for value in values[i]:
            bin_address = bin(int(re.search('\[([^\)]+)\]', value).group(1)))[2:].zfill(36)
            masked_address = ''.join(bit if bit != '0' else bin_address[index] for index, bit in enumerate(mask))
            for combination in product('01', repeat=masked_address.count('X')):
                bin_address = masked_address
                for bit in combination:
                    bin_address = bin_address.replace('X', bit, 1)
                memory[int(bin_address, 2)] = int(re.search('\=(.*)', value).group(1)[1:])
    return sum(memory.values())
part1()
part2()