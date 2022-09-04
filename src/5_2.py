import numpy as np


def register_points(x1, y1, x2, y2, m):
    """Receives a line denoted by (x1, y1) and (x2, y2),
    increases the count in the matrix for all points
    in that line."""

    # Lines can be horizontal, vertical (x1 == x2 or y1 == y2) or diagonal (45 degrees).

    if x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1
        for i in range(y1, y2 + 1):
            m[x1][i] += 1
        return

    if y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1
        for i in range(x1, x2 + 1):
            m[i][y1] += 1
        return

    # Not horizontal nor vertical.

    """ Determine the point 1 with the smallest x.
    If the other point has a larger y, increase both x and y to arrive at point 2.
    Else, increase x and decrease y. """

    point_1 = (x1, y1)
    point_2 = (x2, y2)

    point_2_has_larger_y = True

    if x1 > x2:
        point_1, point_2 = point_2, point_1

    if point_2[1] < point_1[1]:
        point_2_has_larger_y = False

    while point_1 != point_2:
        m[point_1[0]][point_1[1]] += 1

        if point_2_has_larger_y:
            point_1 = (point_1[0] + 1, point_1[1] + 1)
        else:
            point_1 = (point_1[0] + 1, point_1[1] - 1)

    m[point_1[0]][point_1[1]] += 1  # last one for when p1 reaches p2.


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
