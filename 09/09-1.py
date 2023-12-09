from utilities import success, get_input

input = get_input()


def get_diffs(numbers):
    return [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]


total = 0
for line in input:
    numbers = list(map(int, line.split()))

    pyramid = [numbers]

    while pyramid[-1][0] != 0 or pyramid[-1][1] != 0:
        pyramid.append(get_diffs(pyramid[-1]))

    for i in reversed(range(len(pyramid) - 1)):
        pyramid[i].append(pyramid[i][-1] + pyramid[i + 1][-1])

    total += pyramid[0][-1]


success(total)
