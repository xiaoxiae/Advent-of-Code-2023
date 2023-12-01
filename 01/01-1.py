from utilities import success, get_input

input = get_input()


total = 0
for line in input:
    numerics = [c for c in line if c.isnumeric()]
    total += int(numerics[0] + numerics[-1])

success(total)


