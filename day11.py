with open('Day11.txt') as f:
    inputs = f.read()
seats = {}
height, width = 0, 0
for row, line in enumerate(inputs.splitlines()):
    height += 1
    width = max(len(line), width)
    for col, value in enumerate(line):
        if value == '.':
            continue
        seats[row, col] = (value == '#')
(height, width)
def find_stable(data, rule, display=False):
    loops = 0
    previous = data
    while True:
        current = {coords: rule(previous, coords) for coords in previous}
        loops += 1
        if current == previous:
            return loops, sum(current.values())
        previous = current

shifts = ((+1, +1), (+1, +0), (+1, -1), (+0, +1), (+0, -1), (-1, +1), (-1, +0), (-1, -1))
def rule1(data, coords):
    row, col = coords
    value = data[row, col]
    neighbours = 0
    for shift_row, shift_col in shifts:
        i, j = row + shift_row, col + shift_col
        if (i, j) in data:
            neighbours += data[i, j]
    return (not value and not neighbours) or (value and neighbours < 4)

def rule2(data, coords):
    row, col = coords
    value = data[row, col]
    neighbours = 0
    for shift_row, shift_col in shifts:
        i, j = row + shift_row, col + shift_col
        while i >= 0 and j >= 0 and i < height and j < width:
            if (i, j) in data:
                neighbours += data[i, j]
                break
            i, j = i + shift_row, j + shift_col
    return (not value and not neighbours) or (value and neighbours < 5)

print(find_stable(seats,rule=rule2))