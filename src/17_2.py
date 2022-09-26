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
    px, py = 0, 0
    while (px <= x2 and py >= y1):
        px, py, vx, vy = step(px, py, vx, vy)
        if in_target(px, py, x1, x2, y1, y2):
            print(f"Hit target at {(px, py)}, initials {(init_vx, init_vy)}")
            return True
    return False


x1, x2, y1, y2 = [int(i) for i in re.findall("-?\d+", input())]
cnt = 0
for i in range(1000):
    for j in range(-1000, 1000):
        if shoot(i, j, x1, x2, y1, y2):
            cnt += 1
print(cnt)
