import statistics

def fuel_a_to_b(a, b):
    n = abs(a - b)
    return 0.5 * n * (n + 1)

def calculate_fuel_to_position(numbers, pos):
    fuel = 0
    for i in numbers:
        fuel += fuel_a_to_b(i, pos)
    return fuel

with open('input7', 'r') as f:
    numbers = [int(i) for i in f.read().split(',')]

start_at = min(numbers)
end_at = max(numbers)
fuels = []

for i in range(start_at, end_at + 1):
    fuels.append(calculate_fuel_to_position(numbers, i))

print(min(fuels))
