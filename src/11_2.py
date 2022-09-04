import sys

matrix = []
flashes = 0


def count_zeros():
    return sum([i.count(0) for i in matrix])


def flash(j, k):
    matrix[j][k] = 0
    for a in range(j - 1, j + 2):
        for b in range(k - 1, k + 2):
            if (
                a >= 0
                and a < len(matrix)
                and b >= 0
                and b < len(matrix[0])
                and (a != j or b != k)
                and matrix[a][b] != 0
            ):
                matrix[a][b] += 1
                if matrix[a][b] == 10:
                    flash(a, b)


for row in sys.stdin:
    matrix.append([int(i) for i in row.strip()])

i = 1

while True:
    matrix = [[n + 1 for n in row] for row in matrix]
    for j in range(len(matrix)):
        for k in range(len(matrix[0])):
            if matrix[j][k] > 9:
                flash(j, k)

    if count_zeros() == len(matrix) * len(matrix[0]):
        break
    i += 1

print(i)
