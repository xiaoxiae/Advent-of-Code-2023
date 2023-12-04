from utilities import success, get_input
from collections import defaultdict

input = get_input()

for i in range(len(input)):
    input[i] = "." + input[i] + "."
input = ["." * len(input[0])] + input + ["." * len(input[0])]


def get_nearby_gears(x, y) -> set[tuple[int, int]]:
    gears = set()
    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1),
                   (-1, 1), (1, -1), (-1, -1), (1, 1)]:
        nx, ny = x + dx, y + dy

        if input[ny][nx] == "*":
            gears.add((nx, ny))
    return gears


gear_dict = defaultdict(list)
for y in range(len(input)):
    start = None
    nearby_gears = set()

    for x in range(len(input[y])):
        if input[y][x].isnumeric():
            if start is None:
                start = x
            nearby_gears |= get_nearby_gears(x, y)
        else:
            if start is not None and len(nearby_gears) != 0:
                for gear in nearby_gears:
                    gear_dict[gear].append(int(input[y][start:x]))
            start = None
            nearby_gears = set()


total = 0
for nums in gear_dict.values():
    if len(nums) == 2:
        total += nums[0] * nums[1]

success(total)
