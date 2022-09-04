import statistics


def calculate_fuel_to_best_position(numbers):
    align_at = statistics.median(numbers)
    fuel = 0
    for i in numbers:
        fuel += abs(i - align_at)
    return fuel


with open("input7", "r") as f:
    numbers = [int(i) for i in f.read().split(",")]

print(calculate_fuel_to_best_position(numbers))
