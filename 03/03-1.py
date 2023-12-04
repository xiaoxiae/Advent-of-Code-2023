from utilities import success, get_input

input = get_input()

for i in range(len(input)):
    input[i] = "." + input[i] + "."
input = ["." * len(input[0])] + input + ["." * len(input[0])]


def is_near_symbol(x, y) -> bool:
    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1),
                   (-1, 1), (1, -1), (-1, -1), (1, 1)]:
        nx, ny = x + dx, y + dy

        if not input[ny][nx].isnumeric() and input[ny][nx] != ".":
            return True
    return False


total = 0
for y in range(len(input)):
    start = None
    is_valid = False

    for x in range(len(input[y])):
        if input[y][x].isnumeric():
            if start is None:
                start = x
            is_valid = is_valid or is_near_symbol(x, y)
        else:
            if start is not None and is_valid:
                total += int(input[y][start:x])
            start = None
            is_valid = False

success(total)
