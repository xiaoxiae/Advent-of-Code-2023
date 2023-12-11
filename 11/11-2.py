from utilities import success, get_input
from itertools import combinations

input = get_input()


universes = []
for y, row in enumerate(input):
    for x, c in enumerate(row):
        if c == "#":
            universes.append((x, y))

empty_rows = set()
for y, row in enumerate(input):
    if "#" not in row:
        empty_rows.add(y)

empty_columns = set()
for x in range(len(input[0])):
    column = [input[y][x] for y in range(len(input))]
    if "#" not in column:
        empty_columns.add(x)

total = 0
expansions = 1000000 - 1
for (x1, y1), (x2, y2) in combinations(universes, r=2):

    distance = 0
    for x in range(min(x1, x2), max(x1, x2)):
        if x in empty_columns:
            distance += expansions
        distance += 1

    for y in range(min(y1, y2), max(y1, y2)):
        if y in empty_rows:
            distance += expansions
        distance += 1

    total += distance

success(total)
