from utilities import success, get_input
from functools import cache

input = get_input()


@cache
def count_ways(record: str, groups: tuple) -> int:
    def can_be_eaten():
        return "." not in record[:groups[0]] \
                and (len(record) == groups[0] or record[groups[0]] in ("?", "."))

    if len(groups) == 0:
        if "#" not in record:
            return 1

        return 0

    if len(record) < groups[0]:
        return 0

    # for functional, just recurse
    if record[0] == ".":
        return count_ways(record.lstrip("."), groups)

    # for spring, we must eat a group
    elif record[0] == "#":
        if can_be_eaten():
            return count_ways(record[groups[0]+1:], groups[1:])

        return 0

    # for dot, we can either act like it's a dot or a spring
    else:
        dot_result = count_ways(record[1:], groups)
        hash_result = 0

        if can_be_eaten():
            hash_result = count_ways(record[groups[0]+1:], groups[1:])

        return dot_result + hash_result



total = 0
for row in input:
    records, groups_str = row.split()
    groups = tuple(map(int, groups_str.split(",")))

    unfolded_records = "?".join([records] * 5)
    unfolded_groups = groups * 5

    total += count_ways(unfolded_records, unfolded_groups)

success(total)
