from utilities import success, get_input

input = get_input()

instructions = input[0]

graph = {}
for line in input[2:]:
    f, _, l, r = line.split()
    l, r = l[1:-1], r[:-1]

    graph[f] = (l, r)


current = "AAA"
i = 0
while current != "ZZZ":
    j = 0 if instructions[i % len(instructions)] == "L" else 1
    current = graph[current][j]
    i += 1

success(i)
