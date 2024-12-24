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


def get_neighbours(pos, neighbours, steps=1):
    if steps == 0:
        return neighbours
    for _x, _y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        next = (pos[0] + _x, pos[1] + _y)
        if next not in neighbours:
            neighbours.add(next)
            get_neighbours(next, steps=steps - 1, neighbours=neighbours)
    return neighbours


diff = 50
count = 0
start = find_s()
end = find_e()

shortest_path = run()
neighbours: Set[Tuple[int, int]] = set()
get_neighbours((0, 0), steps=6, neighbours=neighbours)
for x, y in shortest_path.keys():
    for _x, _y in neighbours:
        next = (x + _x, y + _y)
        if (x, y) == start and (_x, _y) == (2, 4):
            print((shortest_path[next] - shortest_path[(x, y)] - abs(_x) - abs(_y)))
        if (
            next in shortest_path
            and (shortest_path[next] - shortest_path[(x, y)] - abs(_x) - abs(_y))
            == diff
        ):
            count += 1

print(count)
