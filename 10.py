def corrupted(line):
    ''' Returns 0 if not corrupted.'''
    ''' Returns the score of the illegal character otherwise. '''
    symbols = {'(': ')', '[': ']', '{': '}', '<': '>'}
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    stack = []

    for c in line:
        if c in symbols.keys():
            stack.append(c)
        else:
            try:
                p = stack.pop()
            except IndexError:
                print('Line incomplete')
                return 0
            if c != symbols[p]:
                print(f'Expected {symbols[p]}, found {c}')
                return scores[c]

    return 0


with open('input10', 'r') as f:
    lines = f.read().splitlines()

s = 0

for l in lines:
    print(s)
    s += corrupted(l)

print(s)
