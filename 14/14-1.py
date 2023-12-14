from utilities import success, get_input
from functools import cache

input = list(map(list, get_input()))


def _slide(array, p, direction):
    x, y = p
    if array[y][x] != "O":
        return

    n = len(array)

    nx, ny = x, y
    while 0 <= nx < n and 0 <= ny < n:
        nx += direction[0]
        ny += direction[1]

        if array[ny][nx] != ".":
            break

    nx -= direction[0]
    ny -= direction[1]

    array[y][x], array[ny][nx] = array[ny][nx], array[y][x]


def slide(array, direction):
    n = len(array)

    x = 0 if direction[0] in (0, -1) else (n - 1)
    y = 0 if direction[1] in (0, -1) else (n - 1)
    k = 0 if direction[0] != 0 else 1

    for i in range(n):
        dx, dy = -direction[0] * i, -direction[1] * i

        for j in range(n):
            new = [x + dx, y + dy]
            new[1-k] += j

            _slide(array, new, direction)


slide(input, (0, -1))

total = 0
for i, row in enumerate(input):
    total += row.count("O") * (len(row) - i)

success(total)

