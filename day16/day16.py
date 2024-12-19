# Implement A*

from typing import Dict, Tuple
from pathlib import Path

map = Path("./input.txt").read_text().split("\n")


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


end = find_e()
fringe = [(0, find_s(), (1, 0))]
lowest_score: Dict[Tuple[Tuple[int, int], Tuple[int, int]], int] = dict()
current: Tuple[int, Tuple[int, int], Tuple[int, int]] = fringe.pop()

print(end)

while current and current[1] != end:
    score, (x, y), (x_dir, y_dir) = current
    if ((x, y), (x_dir, y_dir)) in lowest_score:
        current = fringe.pop(0)
        continue
    lowest_score[((x, y), (x_dir, y_dir))] = score

    (x_dir_new, y_dir_new) = (x_dir, y_dir)
    (x_new, y_new) = (x + x_dir_new, y + y_dir_new)
    if map[y_new][x_new] != "#":
        fringe.append((score + 1, (x_new, y_new), (x_dir_new, y_dir_new)))

    # Left turn
    (x_dir_new, y_dir_new) = (y_dir, -x_dir)
    (x_new, y_new) = (x + x_dir_new, y + y_dir_new)
    if map[y_new][x_new] != "#":
        fringe.append((score + 1001, (x_new, y_new), (x_dir_new, y_dir_new)))

    # Right turn
    (x_dir_new, y_dir_new) = (-y_dir, x_dir)
    (x_new, y_new) = (x + x_dir_new, y + y_dir_new)
    if map[y_new][x_new] != "#":
        fringe.append((score + 1001, (x_new, y_new), (x_dir_new, y_dir_new)))

    fringe = sorted(set(fringe))
    current = fringe.pop(0)

# Fastest path
print(current)

# Backtracking
