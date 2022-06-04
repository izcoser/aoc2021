def has_all(a, b):
    ''' Returns true if all characters of b are in a. '''
    for c in b:
        if not (c in a):
            return False
    return True

def patterns_to_numbers(patterns):
    ''' Receives a list of strings encoding numbers from 0 to 9.
        Returns a dictionary mapping each pattern to the corresponding int. '''

    numbers = {}
    numbers[1] = [p for p in patterns if len(p) == 2].pop()
    numbers[4] = [p for p in patterns if len(p) == 4].pop()
    numbers[7] = [p for p in patterns if len(p) == 3].pop()
    numbers[8] = [p for p in patterns if len(p) == 7].pop()

    patterns.remove(numbers[1])
    patterns.remove(numbers[4])
    patterns.remove(numbers[7])
    patterns.remove(numbers[8])

    numbers[3] = [p for p in patterns if len(p) == 5 and has_all(p, numbers[7])].pop()
    patterns.remove(numbers[3])

    numbers[6] = [p for p in patterns if len(p) == 6 and not has_all(p, numbers[7])].pop()
    patterns.remove(numbers[6])

    numbers[9] = [p for p in patterns if len(p) == 6 and has_all(p, numbers[3])].pop()
    patterns.remove(numbers[9])
    numbers[0] = [p for p in patterns if len(p) == 6].pop()
    patterns.remove(numbers[0])

    numbers[5] = [p for p in patterns if len(p) == 5 and has_all(numbers[9], p)].pop()
    patterns.remove(numbers[5])
    numbers[2] = patterns.pop()

    numbers = {v: k for k, v in numbers.items()} # invert..

    return numbers

with open('input8', 'r') as f:
    lines = f.readlines()

s = 0

for line in lines:
    patterns = [''.join(sorted(n)) for n in line.split('|')[0].strip().split()]
    outputs = [''.join(sorted(n)) for n in line.split('|')[1].strip().split()]
    numbers = patterns_to_numbers(patterns)
    output_digits = [numbers[output] for output in outputs]
    output_value = output_digits[0] * 1000 + output_digits[1] * 100 + output_digits[2] * 10 + output_digits[3]
    s += output_value

print(s)
