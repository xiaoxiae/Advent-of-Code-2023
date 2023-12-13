from utilities import success, get_input
from functools import cache

input = get_input(whole=True).split("\n\n")


def _reflective(array, row):
    for i in range(min(row + 1, len(array) - row - 1)):
        if array[row - i] != array[row + i + 1]:
            return False
    return True

def reflective_scores(pattern):
    for i in range(len(pattern) - 1):
        if _reflective(pattern, i):
            yield (i + 1) * 100

    pattern = transpose(pattern)

    for i in range(len(pattern) - 1):
        if _reflective(pattern, i):
            yield i + 1

def smudged_reflective_score(pattern):
    pattern = list(map(list, pattern))

    baseline = set(reflective_scores(pattern))
    for y in range(len(pattern)):
        for x in range(len(pattern[0])):
            pattern[y][x] = "." if pattern[y][x] == "#" else "#"

            new = set(reflective_scores(pattern))
            if new and new != baseline:
                return list(new - baseline)[0]

            pattern[y][x] = "." if pattern[y][x] == "#" else "#"

def transpose(array):
    return list(zip(*array))


total = 0
for pattern in input:
    total += smudged_reflective_score(pattern.splitlines())


success(total)
