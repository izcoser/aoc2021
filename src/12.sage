import sys

paths = []


def explore(G, parent, node, path, visits):
    # print(f'exploring {node}, path={path}, parent={parent}')

    if node not in visits:
        visits[node] = 1
    else:
        visits[node] += 1

    if node == "end":
        paths.append(path)
        return

    for n in [x for x in G.neighbors(node) if x != "start"]:
        if n not in visits or not (visits[n] == 1 and n.islower()):
            v = visits.copy()
            explore(G, node, n, path + "," + n, v)


G = Graph()
for line in sys.stdin:
    line = line.strip()
    v1, v2 = line.split("-")
    G.add_edge((v1, v2), label=line)

visits = {}
explore(G, "", "start", "start", visits)
print(len(paths))
