import sys

m = []

def inMatrix(i, j):
    return i >= 0 and i < len(m) and j >= 0 and j < len(m[0])

g = DiGraph(weighted=True)

for line in sys.stdin:
    m.append([int(i) for i in line.strip()])

for i in range(len(m)):
    for j in range(len(m[0])):
        neighbors = [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]
        for k in neighbors:
            if inMatrix(k[0], k[1]):
                g.add_edge(((i, j), k), label=m[ k[0] ][ k[1] ])

start = (0, 0)
end = (len(m) - 1, len(m[0]) - 1)
print(g.shortest_path_length(start, end, by_weight=True))
