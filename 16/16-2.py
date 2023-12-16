from utilities import success, get_input

input = list(map(list, get_input(whole=True).strip().splitlines()))


def bfs(start, direction):
    visited = set()
    queue = [(start, direction)]

    while len(queue) != 0:
        s = queue.pop()  # care, not queue atm

        if s in visited:
            continue

        visited.add(s)

        (x, y), (dx, dy) = s
        nx, ny = x + dx, y + dy

        # skip out of bounds
        if not (0 <= nx < len(input[0]) and 0 <= ny < len(input)):
            continue

        # split |
        if input[ny][nx] == "|" and dx != 0:
            queue.append(((nx, ny), (0, 1)))
            queue.append(((nx, ny), (0, -1)))
            continue

        # split -
        if input[ny][nx] == "-" and dy != 0:
            queue.append(((nx, ny), (1, 0)))
            queue.append(((nx, ny), (-1, 0)))
            continue

        # reflect /
        if input[ny][nx] == "/":
            queue.append(((nx, ny), (-dy, -dx)))
            continue

        # reflect \
        if input[ny][nx] == "\\":
            queue.append(((nx, ny), (dy, dx)))
            continue

        # continue
        queue.append(((nx, ny), (dx, dy)))


    return len(set(v for v, _ in visited))


max_energy = 0

for x in range(len(input[0])):
    max_energy = max(max_energy, bfs((x, -1), (0, 1)) - 1)
    max_energy = max(max_energy, bfs((x, len(input)), (0, -1)) - 1)

for y in range(len(input)):
    max_energy = max(max_energy, bfs((-1, y), (1, 0)) - 1)
    max_energy = max(max_energy, bfs((len(input[0]), y), (-1, 0)) - 1)

success(max_energy)
