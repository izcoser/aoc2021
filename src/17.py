import re


def decrease_vx(vx):
    return (vx - 1) if vx > 0 else ((vx + 1) if vx < 0 else 0)


def step(px, py, vx, vy):
    px += vx
    py += vy
    vx = decrease_vx(vx)
    vy -= 1
    return (px, py, vx, vy)


def in_target(px, py, x1, x2, y1, y2):
    return x1 <= px and x2 >= px and y1 <= py and y2 >= py


def shoot(vx, vy, x1, x2, y1, y2):
    init_vx, init_vy = vx, vy
    max_y = float("-INF")
    px, py = 0, 0
    while (px <= x2 and py >= y1):
        px, py, vx, vy = step(px, py, vx, vy)
        max_y = max(max_y, py)
        if in_target(px, py, x1, x2, y1, y2):
            print(f"Hit target at {(px, py)}, initials {(init_vx, init_vy)}")
            return max_y
    return float("-INF")


x1, x2, y1, y2 = [int(i) for i in re.findall("-?\d+", input())]
max_y = float("-INF")
for i in range(1000):
    for j in range(1000):
        max_y = max(max_y, shoot(i, j, x1, x2, y1, y2))

print(max_y)
