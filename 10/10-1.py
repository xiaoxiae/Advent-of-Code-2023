from utilities import success, get_input

from collections import defaultdict

input = get_input()


connection_types = {
    ("-"):  ((-1, 0), (1, 0)),
    ("|"):  ((0, 1), (0, -1)),
    ("L"):  ((0, -1), (1, 0)),
    ("J"):  ((0, -1), (-1, 0)),
    ("F"):  ((0, 1), (1, 0)),
    ("7"):  ((0, 1), (-1, 0)),
    ("S"):  ((1, 0), (0, 1), (-1, 0), (0, -1)),
}


graph = defaultdict(list)
start = None
for y in range(len(input)):
    for x in range(len(input[0])):
        if input[y][x] == ".":
            continue

        if input[y][x] == "S":
            start = (x, y)

        for dx, dy in connection_types[input[y][x]]:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < len(input[0]) and 0 <= ny < len(input)):
                continue

            if input[ny][nx] == ".":
                continue

            # matching connection
            if (-dx, -dy) not in connection_types[input[ny][nx]]:
                continue

            graph[x, y].append((nx, ny))


# strip non-loop nodes
while True:
    deleted = False

    for k in list(graph):
        if len(graph[k]) == 1:
            deleted = True
            del graph[k]

    if not deleted:
        break


queue = [(0, start)]
explored = {start: 0}
max_distance = 0
while len(queue) != 0:
    d, current = queue.pop(0)
    max_distance = max(max_distance, d)

    for neighbour in graph[current]:
        if neighbour in explored:
            continue

        explored[neighbour] = d + 1
        queue.append((d + 1, neighbour))


success(max_distance)
