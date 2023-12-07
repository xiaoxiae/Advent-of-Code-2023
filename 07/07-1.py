from utilities import success, get_input
from itertools import groupby

input = get_input()
for i in range(len(input)):
    input[i] = input[i].split()

strength = "23456789TJQKA"


def kind(hand: str) -> int:
    hand = sorted(list(hand))

    occurrences = sorted([len(list(o)) for _, o in groupby(hand)], reverse=True)

    if occurrences[0] == 5:
        return 6
    elif occurrences[0] == 4:
        return 5
    elif occurrences[0] == 3 and occurrences[1] == 2:
        return 4
    elif occurrences[0] == 3:
        return 3
    elif occurrences[0] == 2 and occurrences[1] == 2:
        return 2
    elif occurrences[0] == 2:
        return 1
    else:
        return 0

input = sorted(
    input,
    key=lambda x: (kind(x[0]), [strength.index(c) for c in x[0]]),
)

total = 0
for i in range(len(input)):
    total += (i + 1) * int(input[i][1])

success(total)
