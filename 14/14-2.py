from utilities import success, get_input
from functools import cache

input = list(map(list, get_input()))


def _slide(array, p, direction):
    x, y = p
    if array[y][x] != "O":
        return

    n = len(array)

    nx, ny = x, y
    while True:
        nx += direction[0]
        ny += direction[1]

        if not (0 <= nx < n and 0 <= ny < n) or array[ny][nx] != ".":
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


def cycle(array):
    for d in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        slide(array, d)


i = 0
visited = {}
while True:
    cycle(input)
    input_hash = "".join(["".join(row) for row in input])

    i += 1

    if input_hash in visited:
        break

    visited[input_hash] = i

start = visited[input_hash]
period = i - start

n = 1_000_000_000

for _ in range((n - start) % period):
    cycle(input)

total = 0
for i, row in enumerate(input):
    total += row.count("O") * (len(row) - i)

success(total)
