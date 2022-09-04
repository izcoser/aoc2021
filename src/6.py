import numpy as np


def pass_day(fish):
    """Makes a one day progress in the fish array."""
    fish -= 1
    fish_to_add = 0
    for idx, f in enumerate(fish):
        if f == -1:
            fish[idx] = 6
            fish_to_add += 1

    return np.concatenate((fish, np.array([8] * fish_to_add)), axis=0)


with open("input6", "r") as f:
    fish = np.fromstring(f.readline().strip(), dtype=np.int32, sep=",")

for i in range(80):
    fish = pass_day(fish)

print(len(fish))
