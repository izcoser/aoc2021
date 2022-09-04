def most_common_nth_bit(lines, n):
    """Receives lines, returns the most common nth bit from left to right."""
    count = 0
    for line in lines:
        count += int(line[n])

    if count / len(lines) >= 0.5:
        return "1"
    else:
        return "0"


with open("input3", "r") as f:
    lines_a = f.read().splitlines()

lines_b = lines_a.copy()

searching_a = True
searching_b = True

for i in range(12):
    nth_bit = i
    most_common_a = most_common_nth_bit(lines_a, nth_bit)
    most_common_b = most_common_nth_bit(lines_b, nth_bit)
    if searching_a:
        lines_a = [line for line in lines_a if line[i] == most_common_a]

    if searching_b:
        lines_b = [line for line in lines_b if line[i] != most_common_b]

    if len(lines_a) == 1:
        searching_a = False

    if len(lines_b) == 1:
        searching_b = False

a = int(lines_a[0], 2)
b = int(lines_b[0], 2)

print(a * b)
