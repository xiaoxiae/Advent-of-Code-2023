from utilities import success, get_input

input = get_input()


cards = [1] * len(input)

total = 0
for i, line in enumerate(input):
    print(i)
    numbers = line.split(maxsplit=2)[-1]

    winning_str, have_str = numbers.split(" | ")

    winning = set(map(int, winning_str.split()))
    have = set(map(int, have_str.split()))

    n = len(winning & have)

    for j in range(i + 1, i + n + 1):
        cards[j] += cards[i]

success(sum(cards))
