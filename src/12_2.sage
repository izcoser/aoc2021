import sys

paths = []


def a_small_cave_has_been_visited_twice(visits):
    for v in visits:
        if visits[v] == 2 and v.islower():
            return True
    return False


def explore(G, parent, node, path, visits):
    # print(f'exploring {node}, path={path}, parent={parent}')

    visits[node] += 1

    if node == "end":
        paths.append(path)
        return

    for n in [x for x in G.neighbors(node) if x != "start"]:
        if not (
            n.islower()
            and a_small_cave_has_been_visited_twice(visits)
            and visits[n] > 0
        ):
            v = visits.copy()
            explore(G, node, n, path + "," + n, v)


G = Graph()
for line in sys.stdin:
    line = line.strip()
    v1, v2 = line.split("-")
    G.add_edge((v1, v2), label=line)

visits = {}
for v in G.get_vertices():
    visits[v] = 0

explore(G, "", "start", "start", visits)
print(len(paths))
