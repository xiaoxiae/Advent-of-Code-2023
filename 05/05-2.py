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
seed_ranges = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]

while t != "location":
    ranges = dicts[t]
    t = list(dicts[t])[0]

    new_seed_ranges = []
    i = 0
    while i < len(seed_ranges):
        sl, sh = seed_ranges[i]

        for l, h in ranges[t]:
            # no overlap - continue
            if sh < l or h < sl:
                continue

            # seeds are all within range - no split, just map
            if l <= sl <= sh <= h:
                new_seed_ranges.append(
                    (
                        ranges[t][(l, h)] + (sl - l),
                        ranges[t][(l, h)] + (sh - l),
                    )
                )
                break

            # otherwise split into parts, add to seed ranges and continue
            else:
                if sl < l:
                    seed_ranges.append((sl, l - 1))
                if h < sh:
                    seed_ranges.append((h + 1, sh))
                seed_ranges.append((max(sl, l), min(sh, h)))
                break
        else:
            new_seed_ranges.append((sl, sh))

        i += 1

    seed_ranges = new_seed_ranges


success(min([l for l, _ in seed_ranges]))
