from utilities import success, get_input

input = get_input()


def power(line):
    minimum = {"red": 0, "green": 0, "blue": 0}

    for part in line.split(": ", 1)[1].split("; "):
        for instance in part.split(", "):
            count, color = instance.split()

            minimum[color] = max(minimum[color], int(count))

    total = 1
    for count in minimum.values():
        total *= count

    return total


total_power = 0
for line in input:
    total_power += power(line)

success(total_power)
