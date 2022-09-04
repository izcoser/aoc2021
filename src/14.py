import sys
import collections

template = input().strip()
input()

rules = {}

for line in sys.stdin:
    line = line.strip()
    key, value = line.split(" -> ")
    rules[key] = key[0] + value + key[1]

for _ in range(10):
    i = 0
    while i < len(template) - 1:
        # print(f'{template}, len: {len(template)}, i = {i}')
        key = template[i : i + 2]
        if key in rules:
            template = template[0:i] + rules[key] + template[i + 2 :]
            i += 1
        i += 1
    # print(template)

counts = collections.Counter(template).most_common()
print(counts[0][1] - counts[-1][1])
