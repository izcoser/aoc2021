def pass_day(fish):
    """Makes a one day progress in the fish array."""
    fish_copy = fish.copy()

    for i in range(7, -1, -1):
        fish[i] = (i, fish_copy[i + 1][1])

    fish[6] = (6, fish[6][1] + fish_copy[0][1])
    fish[8] = (8, fish_copy[0][1])


with open("input6", "r") as f:
    numbers = [int(i) for i in f.readline().strip().split(",")]

fish = [(i, 0) for i in range(9)]

for idx, _ in enumerate(fish):
    fish[idx] = (idx, numbers.count(idx))

for i in range(256):
    pass_day(fish)

print(sum([i[1] for i in fish]))
