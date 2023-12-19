from utilities import success, get_input


x, y = 0, 0
deltas = {"R": (1, 0), "D": (0, -1), "L": (-1, 0), "U": (0, 1)}
delta_order = ["R", "D", "L", "U"]
prev_dir = None

points = []
for line in get_input():
    hex = line.split()[-1][2:-1]
    dir = delta_order[int(hex[-1])]
    d = int(hex[:-1], 16)

    if prev_dir == "R" and dir == "D":
        x += 1
    elif prev_dir == "D" and dir == "L":
        y -= 1
    elif prev_dir == "L" and dir == "U":
        x -= 1
    elif prev_dir == "U" and dir == "R":
        y += 1

    points.append((x, y))

    dx, dy = deltas[dir]
    x += dx * d
    y += dy * d

    if prev_dir == "R" and dir == "U":
        y -= 1
    elif prev_dir == "U" and dir == "L":
        x += 1
    elif prev_dir == "L" and dir == "D":
        y += 1
    elif prev_dir == "D" and dir == "R":
        x -= 1

    prev_dir = dir

points.append((x, y))


total = 0
for i in range(len(points)):
    (x1, y1), (x2, y2) = points[i-1], points[i]

    if y1 == y2:
        total += (x1 - x2) * y1

success(abs(total))
