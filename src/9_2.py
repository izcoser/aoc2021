import numpy as np

N = 10


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


def flood_fill(m, x, y):
    if m[x][y] >= 9:
        return

    m[x][y] = N

    if x > 0:
        flood_fill(m, x - 1, y)
    if x < m.shape[0] - 1:
        flood_fill(m, x + 1, y)
    if y > 0:
        flood_fill(m, x, y - 1)
    if y < m.shape[1] - 1:
        flood_fill(m, x, y + 1)

    return


with open("input9", "r") as f:
    lines = f.read().splitlines()

m = np.array([[int(n) for n in line] for line in lines], dtype=np.uint32)
basins = []

for i in range(m.shape[0]):
    for j in range(m.shape[1]):
        if low_point(m, i, j):
            flood_fill(m, i, j)
            s = (m == N).sum()
            if s > 0:
                basins.append(s)
            N += 1

basins.sort()
print(np.prod(basins[-3:]))
