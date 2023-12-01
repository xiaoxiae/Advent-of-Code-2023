from utilities import success, get_input

input = get_input()


digits = [ "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]

total = 0
for line in input:
    numbers = []
    for i in range(len(line)):
        if line[i].isnumeric():
            numbers.append(int(line[i]))
            continue

        for j, digit in enumerate(digits):
            if line[i:i+len(digit)] == digit:
                numbers.append(j+1)
                break

    total += 10 * numbers[0] + numbers[-1]

success(total)


