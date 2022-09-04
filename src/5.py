import numpy as np


def register_points(x1, y1, x2, y2, m):
    """Receives a line denoted by (x1, y1) and (x2, y2),
    increases the count in the matrix for all points
    in that line."""

    # Lines are only horizontal or vertical (x1 == x2 or y1 == y2).

    if x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1
        for i in range(y1, y2 + 1):
            m[x1][i] += 1

    if y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1
        for i in range(x1, x2 + 1):
            m[i][y1] += 1


m = np.zeros((1000, 1000), dtype=np.int32)

with open("input5", "r") as f:
    while True:
        s = f.readline().strip()
        if s == "":
            break
        else:
            x1, y1, x2, y2 = [int(n) for n in s.replace(" -> ", ",").split(",")]
            register_points(x1, y1, x2, y2, m)

print(np.sum(m >= 2))
