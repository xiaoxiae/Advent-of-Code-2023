from utilities import success, get_input

from collections import defaultdict
import heapq

input = [[int(c) for c in l] for l in get_input()]


def heuristic(x, y):
    return abs(x - ex) + abs(y - ey)


ex, ey = len(input[0]) - 1, len(input) - 1
visited = {((0, 0), (0, 0), 0): None}

#                          d   x  y    dx dy  c
queue = [(heuristic(0, 0), 0, (0, 0), (0, 0), 0)]

while len(queue) != 0:
    _, d, (x, y), (dx, dy), c = heapq.heappop(queue)

    # check all directions
    for (ndx, ndy) in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        # don't go back
        if (dx, dy) == (-ndx, -ndy):
            continue

        # same direction
        if (dx, dy) == (ndx, ndy):
            # don't go forward if c is too large (10)
            if c == 10:
                continue

            nc = c + 1
        else:
            # can't turn in less than 4 (besides start)
            if c <= 3 and (dx, dy) != (0, 0):
                continue

            # otherwise reset counter
            nc = 1

        nx, ny = x + ndx, y + ndy

        # check out of bounds
        if not (0 <= nx < len(input[0]) and 0 <= ny < len(input)):
            continue

        # check if visited
        ns = ((nx, ny), (ndx, ndy), nc)

        if ns in visited:
            continue

        visited[ns] = ((x, y), (dx, dy), c)

        nd = d + input[ny][nx]

        if (nx, ny) == (ex, ey) and nc >= 4:
            success(nd)

        heapq.heappush(queue, (nd + heuristic(nx, ny), nd, *ns))
