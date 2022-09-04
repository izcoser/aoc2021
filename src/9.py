import numpy as np


def adjacent_points(m, x, y):
    adj = []

    for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        try:
            adj.append(
                m[abs(x + i), abs(y + j)]
            )  # negative indexes will not throw an IndexError.
        except IndexError:
            continue

    return adj


def low_point(m, x, y):
    lower_or_equal_points = [p for p in adjacent_points(m, x, y) if p <= m[x, y]]
    return len(lower_or_equal_points) == 0


with open("input9", "r") as f:
    lines = f.read().splitlines()

m = np.array([[int(n) for n in line] for line in lines], dtype=np.uint8)
low_points = []

for i in range(m.shape[0]):
    for j in range(m.shape[1]):
        if low_point(m, i, j):
            low_points.append(m[i, j])

print(sum(low_points) + len(low_points))
