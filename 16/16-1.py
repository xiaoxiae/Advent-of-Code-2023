from utilities import success, get_input

input = list(map(list, get_input(whole=True).strip().splitlines()))


visited = set()
queue = [((-1, 0), (1, 0))]


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


success(len(set(v for v, _ in visited)) - 1)
