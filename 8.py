def count_1_4_7_8(output):
    c = 0
    for word in output.split():
        if len(word) == 2 or len(word) == 4 or len(word) == 3 or len(word) == 7:
            c += 1

    return c

with open('input8', 'r') as f:
    lines = f.readlines()
    outputs = [line.split('|')[-1].strip() for line in lines]

c = 0

for output in outputs:
    c += count_1_4_7_8(output)

print(c)
