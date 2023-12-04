from utilities import success, get_input

input = get_input()


total = 0
for line in input:
    numbers = line.split(maxsplit=2)[-1]

    winning_str, have_str = numbers.split(" | ")

    winning = set(map(int, winning_str.split()))
    have = set(map(int, have_str.split()))

    n = len(winning & have)

    if n > 0:
        total += 2 ** (n - 1)

success(total)
