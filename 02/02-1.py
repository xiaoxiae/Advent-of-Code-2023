from utilities import success, get_input

input = get_input()


possible = {"red": 12, "green": 13, "blue": 14}


def is_possible(line):
    for part in line.split(": ", 1)[1].split("; "):
        for instance in part.split(", "):
            count, color = instance.split()

            if possible[color] < int(count):
                return False

    return True


possible_games = 0
for i, line in enumerate(input):
    if is_possible(line):
        possible_games += i + 1

success(possible_games)
