from utilities import success, get_input

input = get_input()


times = list(map(int, input[0].split()[1:]))
distances = list(map(int, input[1].split()[1:]))

product = 1
for time, distance in zip(times, distances):
    total = 0
    for i in range(time):
        if i * (time - i) > distance:
            total += 1

    product *= total

success(product)
