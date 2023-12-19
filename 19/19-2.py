from utilities import success, get_input

from dataclasses import dataclass


workflows_str, _ = get_input(whole=True).strip().split("\n\n")

workflows = {}
for line in workflows_str.splitlines():
    label, parts = line.split("{")
    parts = parts[:-1]
    workflows[label] = parts.split(",")


total = 0

def recursive(d, workflow):
    global total

    if workflow == "A":
        local_total = 1
        for a, b in d.values():
            local_total *= (b - a + 1)
        total += local_total

        return

    elif workflow == "R":
        return

    for rule in workflows[workflow]:
        if "<" in rule or ">" in rule:
            symbol = "<" if "<" in rule else ">"

            a, b = rule.split(symbol)
            val, dest = b.split(":")
            val = int(val)

            l, h = d[a]

            # out of range - go to next rule, no recursion
            if (symbol == "<" and l > val) or (symbol == ">" and h < val):
                continue

            # otherwise we limit the range to the one not accepted and recurse
            d_new = dict(d)
            if symbol == "<":
                d_new[a] = (l, val - 1)
                recursive(d_new, dest)
                d[a] = (val, h)
            else:
                d_new[a] = (val + 1, h)
                recursive(d_new, dest)
                d[a] = (l, val)
        else:
            recursive(d, rule)


r = (1, 4000)
d = {"x": r, "m": r, "a": r, "s": r}

recursive(d, "in")

success(total)
