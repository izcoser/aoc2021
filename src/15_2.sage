import sys
import copy

m = []
g = DiGraph(weighted=True)

def inMatrix(i, j):
    return i >= 0 and i < len(m) and j >= 0 and j < len(m[0])

for line in sys.stdin:
    m.append([int(i) for i in line.strip()])

c = copy.deepcopy(m)

for i in range(len(c)):
    for j in range(1, 5):
        m[i] += [k + j if k + j < 10 else k + j - 9 for k in c[i]]

c = copy.deepcopy(m)

for i in range(1, 5):
    for j in range(len(c)):
        m.append([k + i if k + i < 10 else k + i - 9 for k in c[j]])

for i in range(len(m)):
    for j in range(len(m[0])):
        neighbors = [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]
        for k in neighbors:
            if inMatrix(k[0], k[1]):
                g.add_edge(((i, j), k), label=m[ k[0] ][ k[1] ])

start = (0, 0)
end = (len(m) - 1, len(m[0]) - 1)
print(g.shortest_path_length(start, end, by_weight=True))

