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
    fringe = [(0, start)]
    lowest_score = dict()
    current = fringe.pop()

    while current and current[1] != end:
        score, (x, y) = current
        if (x, y) in lowest_score:
            current = fringe.pop(0)
            continue
        lowest_score[(x, y)] = score

        for _x, _y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            (x_new, y_new) = (x + _x, y + _y)
            if (x_new, y_new) not in lowest_score and map[y_new][x_new] != "#":
                fringe.append((score + 1, (x_new, y_new)))

        fringe = sorted(set(fringe))
        current = fringe.pop(0)

    shortest_path = dict()
    while current[1] != start:
        score, (x, y) = current

        for _x, _y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            (x_new, y_new) = (x + _x, y + _y)
            if (x_new, y_new) in lowest_score and score - lowest_score[
                (x_new, y_new)
            ] == 1:
                shortest_path[current[1]] = current[0]
                current = (lowest_score[(x_new, y_new)], (x_new, y_new))
                break

    shortest_path[start] = 0
    return shortest_path


def get_neighbours(pos, neighbours, steps=1):
    if steps == 0:
        return neighbours
    for _x, _y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        next = (pos[0] + _x, pos[1] + _y)
        if next not in neighbours:
            neighbours.add(next)
            get_neighbours(next, steps=steps - 1, neighbours=neighbours)
    return neighbours


chat_steps = 2
diff = 100
count = 0

shortest_path = run()
neighbours: Set[Tuple[int, int]] = set()
get_neighbours((0, 0), steps=2, neighbours=neighbours)
for x, y in shortest_path.keys():
    for _x, _y in neighbours:
        next = (x + _x, y + _y)
        if (
            next in shortest_path
            and (shortest_path[next] - shortest_path[(x, y)] - abs(_x) - abs(_y))
            >= diff
        ):
            count += 1

print(count)
