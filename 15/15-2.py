from utilities import success, get_input

input = get_input(whole=True).strip().split(",")


def hash(string):
    current_value = 0
    for c in string:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256

    return current_value


boxes = [[] for _ in range(256)]


total = 0
for part in input:
    instruction = "-" if part[-1] == "-" else "="
    label = part[:-1] if instruction == "-" else part[:-2]
    box = hash(label)

    if instruction == "-":
        for i in range(len(boxes[box])):
            if boxes[box][i][0] == label:
                boxes[box].pop(i)
                break

    elif instruction == "=":
        value = int(part[-1])

        for i in range(len(boxes[box])):
            if boxes[box][i][0] == label:
                boxes[box][i][1] = value
                break
        else:
            boxes[box].append([label, value])

total = 0
for i, box in enumerate(boxes):
    for j, (_, value) in enumerate(box):
        total += (i + 1) * (j + 1) * value

success(total)
