from utilities import success, get_input

input = get_input(whole=True)


parts = input.split("\n\n")

dicts = {}
for part in parts[1:]:
    lines = part.splitlines()

    f, _, t = lines[0].split()[0].split("-")

    dicts[f] = {t: {}}

    for line in lines[1:]:
        ts, fs, d = list(map(int, line.split()))

        dicts[f][t][(fs, fs + d)] = ts

t = "seed"
seeds = list(map(int, parts[0].split()[1:]))

while t != "location":
    ranges = dicts[t]
    t = list(dicts[t])[0]

    new_seeds = []
    for s in seeds:
        for l, h in ranges[t]:
            if l <= s <= h:
                new_seeds.append(ranges[t][(l, h)] + (s - l))
                break
        else:
            new_seeds.append(s)

    seeds = new_seeds

success(min(seeds))
