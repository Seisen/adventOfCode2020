import re
with open("day16.txt") as f:
    inputs = f.read().splitlines()


def get_conditions(conditions: list = [], i : int = 0):
    """
    :param conditions: list of conditions
    :param i: index
    :return: the le list of all conditions
    """
    try:
        conditions.append(re.search('\:(.*)', inputs[i]).group(1).replace(" ", "").split('or')[0])
        conditions.append(re.search('\:(.*)', inputs[i]).group(1).replace(" ", "").split('or')[1])
        return get_conditions(conditions, i+1)
    except AttributeError:
        return conditions

def get_tickets(key: str,i: int  = 0):
    """
    :param key: string to get the right ticket
    :param i: index
    :return: list of tickets
    """
    if inputs[i] == key:
        if key != "your ticket:":
            return [list(map(int, inputs[j].split(','))) for j in range(i+1, len(inputs))]
        else:
            return list(map(int, inputs[i+1].split(",")))
    else:
        return get_tickets(key,i+1)


conditions, your_ticket, tickets = get_conditions(), get_tickets("your ticket:"), get_tickets("nearby tickets:")

def part1():

    for condition in conditions:
        min, max = map(int, condition.split('-'))

        for ticket in tickets:

            for value in ticket:


                if value <= max and value >= min:

                    ticket.remove(value)

    return sum(sum(ticket) for ticket in tickets)
print(part1())