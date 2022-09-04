import sys

values = {")": 1, "]": 2, "}": 3, ">": 4}


def completion(line):
    """Returns the completion of a line or"""
    """ '' if complete of corrupted. """
    symbols = {"(": ")", "[": "]", "{": "}", "<": ">"}
    stack = []

    for c in line.strip():
        if c in symbols:
            stack.append(c)
        else:
            p = stack.pop()

            if c != symbols[p]:
                return ""

    compl = ""
    while len(stack) > 0:
        compl += symbols[stack.pop()]

    return compl


def score(compl):
    s = 0
    for c in compl:
        s *= 5
        s += values[c]
    return s


scores = []

for line in sys.stdin:
    compl = completion(line)
    s = score(compl)
    if s > 0:
        scores.append(s)
    scores = sorted(scores)

print(scores[int(len(scores) / 2)])
