from utilities import success, get_input
from functools import cache

input = get_input(whole=True).split("\n\n")


def _reflective(array, row):
    for i in range(min(row + 1, len(array) - row - 1)):
        if array[row - i] != array[row + i + 1]:
            return False
    return True

def reflective_score(pattern):
    for i in range(len(pattern) - 1):
        if _reflective(pattern, i):
            return (i + 1) * 100

    pattern = transpose(pattern)

    for i in range(len(pattern) - 1):
        if _reflective(pattern, i):
            return i + 1

def transpose(array):
    return list(zip(*array))


total = 0
for pattern in input:
    total += reflective_score(pattern.splitlines())


success(total)
