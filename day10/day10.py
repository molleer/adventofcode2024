from pathlib import Path
from typing import Set, Tuple

map = Path("./input.txt").read_text().split("\n")
heads = []

for y, line in enumerate(map):
    for x, char in enumerate(line):
        if char == "0":
            heads.append((x, y))


def get_surrounding(pos, map=map):
    neightbours = []
    if pos[0] > 0:
        neightbours.append((pos[0] - 1, pos[1]))
    if pos[1] > 0:
        neightbours.append((pos[0], pos[1] - 1))
    if pos[1] + 1 < len(map):
        neightbours.append((pos[0], pos[1] + 1))
    if pos[0] + 1 < len(map[pos[1]]):
        neightbours.append((pos[0] + 1, pos[1]))
    return neightbours


def _find_tops(start: Tuple[int, int], map):
    fringe: Set[Tuple[Tuple[int, int], ...]] = set([(start,)])
    new_fringe: Set[Tuple[Tuple[int, int], ...]] = set()

    for height in range(9):
        str_height = str(height)
        new_fringe = set()
        for path in fringe:
            (x, y) = path[0]
            if map[y][x] == str_height:
                for neightbour in get_surrounding((x, y), map):
                    new_path = (neightbour, *path)
                    new_fringe.add(new_path)
        fringe = new_fringe
    return fringe


def find_tops1(start: Tuple[int, int], map):
    fringe = _find_tops(start, map)
    return len(
        {path[0] if map[path[0][1]][path[0][0]] == "9" else (-1, -1) for path in fringe}
        - {(-1, -1)}
    )


def find_tops2(start: Tuple[int, int], map):
    fringe = _find_tops(start, map)
    return sum([1 if map[path[0][1]][path[0][0]] == "9" else 0 for path in fringe])


print(sum([find_tops1(pos, map) for pos in heads]))
print(sum([find_tops2(pos, map) for pos in heads]))
