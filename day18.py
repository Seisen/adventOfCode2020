with open("day18.txt") as f:
    inputs = f.readlines()
class Integer(int):
    def __add__(self, other):
        return Integer(int.__add__(self, other))

    def __mul__(self, other):
        return Integer(int.__mul__(self, other))

    __sub__ = __mul__
    __pow__ = __add__

import re

def evaluate(string, replace):
    string = re.sub(r'(\d+)', r'Integer(\1)', string)
    return eval(string.replace(*replace))

print(sum(evaluate(line, replace=('*', '-')) for line in inputs))

print(sum(evaluate(line, replace=('+', '**')) for line in inputs))