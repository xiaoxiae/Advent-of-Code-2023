from utilities import success, get_input
from math import lcm

input = get_input()

instructions = input[0]

graph = {}
for line in input[2:]:
    f, _, l, r = line.split()
    l, r = l[1:-1], r[:-1]

    graph[f] = (l, r)


current = []
for key in graph:
    if key.endswith("A"):
        current.append(key)

i = 0
steps = {}
while len(current) != 0:
    j = 0 if instructions[i % len(instructions)] == "L" else 1
    i += 1

    k = 0
    while k < len(current):
        current[k] = graph[current[k]][j]

        if current[k].endswith("Z"):
            steps[current.pop(k)] = i
        else:
            k += 1

success(lcm(*list(steps.values())))
