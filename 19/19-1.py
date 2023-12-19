from utilities import success, get_input

from dataclasses import dataclass


workflows_str, inputs_str = get_input(whole=True).strip().split("\n\n")

workflows = {}
for line in workflows_str.splitlines():
    label, parts = line.split("{")
    parts = parts[:-1]
    workflows[label] = parts.split(",")

total = 0
for input in inputs_str.splitlines():
    d = {}
    parts = input[1:-1].split(",")
    for part in parts:
        a, b = part.split("=")
        d[a] = int(b)

    workflow = "in"
    while workflow not in ("A", "R"):
        for rule in workflows[workflow]:
            if "<" in rule or ">" in rule:
                symbol = "<" if "<" in rule else ">"
                op = lambda x, y: (x < y) if symbol == "<" else (x > y)

                a, b = rule.split(symbol)
                val, c = b.split(":")

                if op(d[a], int(val)):
                    workflow = c
                    break
            else:
                workflow = rule
                break

    if workflow == "A":
        total += sum(list(d.values()))

success(total)
