from utilities import success, get_input

input = get_input(whole=True).strip().split(",")


def hash(string):
    current_value = 0
    for c in string:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256

    return current_value


total = 0
for part in input:
    total += hash(part)

success(total)
