import sys


def step(rules, pairs):
    new_pairs = {}
    for p in pairs:
        child_1 = p[0] + rules[p[:2]]
        child_2 = rules[p[:2]] + p[1] + "*"
        if "*" in p:
            child_1 += "*"

        count = pairs[p]

        if child_1 not in new_pairs:
            new_pairs[child_1] = count
        else:
            new_pairs[child_1] += count

        if child_2 not in new_pairs:
            new_pairs[child_2] = count
        else:
            new_pairs[child_2] += count
    return new_pairs


def get_char_frequency(pairs):
    char_freq = {}
    for p in pairs:
        first, second = p[0], p[1]

        if second not in char_freq:
            char_freq[second] = pairs[p]
        else:
            char_freq[second] += pairs[p]

        if "*" not in p:
            if first not in char_freq:
                char_freq[first] = pairs[p]
            else:
                char_freq[first] += pairs[p]

    return char_freq


template = input().strip()
input()

rules = {}

for line in sys.stdin:
    line = line.strip()
    key, value = line.split(" -> ")
    rules[key] = value

pairs = {template[:2]: 1}

for i in range(1, len(template) - 1):
    pairs[template[i : i + 2] + "*"] = 1

for _ in range(40):
    pairs = step(rules, pairs)

char_freq = get_char_frequency(pairs)
min_key = min(char_freq, key=char_freq.get)
max_key = max(char_freq, key=char_freq.get)
print(char_freq[max_key] - char_freq[min_key])
