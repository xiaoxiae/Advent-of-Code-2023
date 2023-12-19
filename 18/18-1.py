from utilities import success, get_input


x, y = 0, 0
trench = {(x, y)}
deltas = {"R": (1, 0), "D": (0, -1), "L": (-1, 0), "U": (0, 1)}

for line in get_input():
    dir, d, hex = line.split()
    d = int(d)

    dx, dy = deltas[dir]
    for _ in range(d):
        x += dx
        y += dy
        trench.add((x, y))


queue = [(1, -1)]
while len(queue) != 0:
    x, y = queue.pop()

    for dx, dy in deltas.values():
        nx, ny = x + dx, y + dy

        if (nx, ny) in trench:
            continue

        trench.add((nx, ny))
        queue.append((nx, ny))


success(len(trench))
