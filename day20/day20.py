from typing import Dict, List, Set, Tuple
from pathlib import Path

map: List[List[str]] = [
    list(line) for line in Path("./input.txt").read_text().split("\n")
]


def find_s(map=map) -> Tuple[int, int]:
    for y, line in enumerate(map):
        for x, char in enumerate(line):
            if char == "S":
                return (x, y)
    raise Exception("Cannot find S")


def find_e(map=map) -> Tuple[int, int]:
    for y, line in enumerate(map):
        for x, char in enumerate(line):
            if char == "E":
                return (x, y)
    raise Exception("Cannot find E")


def run(map=map):
    start = find_s()
    end = find_e()
    lowest_score = dict()
    current = start
    count = 0
    lowest_score[start] = count

    while current != end:
        for _x, _y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            (x, y) = current
            new_pos = (x + _x, y + _y)
            if new_pos not in lowest_score and map[new_pos[1]][new_pos[0]] != "#":
                current = new_pos
                break

        count += 1
        lowest_score[current] = count
    return lowest_score


def get_neighbours(n):
    neighbours = set()
    for i in range(n + 1):
        for j in range(n - i + 1):
            neighbours.add((i, j))
            neighbours.add((-i, j))
            neighbours.add((i, -j))
            neighbours.add((-i, -j))
    return neighbours


count = 0
start = find_s()
end = find_e()

savings: Dict[int, Set[Tuple[Tuple[int, int], Tuple[int, int]]]] = dict()

shortest_path = run()
path_length = shortest_path[start]
steps = 20

neighbours = get_neighbours(steps)
assert all([(abs(x) + abs(y)) <= steps for (x, y) in neighbours])

for x, y in shortest_path.keys():
    for _x, _y in neighbours:
        next = (x + _x, y + _y)
        if next in shortest_path:
            short_cut_dist = abs(_x) + abs(_y)
            saved = shortest_path[next] - shortest_path[(x, y)] - short_cut_dist
            savings.setdefault(saved, set()).add(((x, y), next))

for cost_save, saves in sorted(savings.items()):
    if cost_save >= 100:
        count += len(saves)

print(count)
