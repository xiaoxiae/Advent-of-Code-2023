from utilities import success, get_input

input = get_input()


time = int("".join(input[0].split()[1:]))
distance = int("".join(input[1].split()[1:]))

start = 0
for i in range(time):
    if i * (time - i) > distance:
        start = i
        break

for i in reversed(range(time)):
    if i * (time - i) > distance:
        end = i
        break

success(end - start + 1)
