def accumulate_input(line, a):
    """Receives one line of input, increments numbers in the list."""
    for i, c in enumerate(line):
        a[i] += int(c)


def g(a):
    """Receives list of numbers, turns each number into a 0 or 1."""
    """ Parses binary string and returns int."""

    binary_output = [""] * 12
    for i, n in enumerate(a):
        if n > 500:
            binary_output[i] = "1"
        else:
            binary_output[i] = "0"

    return int("".join(binary_output), 2)


with open("input3", "r") as f:
    lines = f.read().splitlines()

# Each line has 12 bits.
# Solution: create a list of 12 numbers (a_11, a_10, ... a_0) each starting at 0.
#   iterate over the lines, adding the value of each bit to the corresponding number.
#   In the end, if a_i > number of lines / 2, a_i = 1. Else a_i = 0.

a = [0] * 12


# print(lines)
for line in lines:
    print(line)
    accumulate_input(line, a)
    print(a)

gamma = g(a)
epsilon = ~gamma & 0xFFF
print(gamma * epsilon)
