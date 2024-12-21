from typing import Dict, List, Set, Tuple
from pathlib import Path

corrupted: List[Tuple[int, int]] = [
    (int(line.split(",")[0]), int(line.split(",")[1]))
    for line in Path("./input.txt").read_text().split("\n")
]


def run(corrupted: Set[Tuple[int, int]]):
    start = (0, 0)
    end = (70, 70)
    fringe = [(0, start)]
    lowest_score: Dict[Tuple[int, int], int] = dict()
    current: Tuple[int, Tuple[int, int]] = fringe.pop()

    while current and current[1] != end:
        score, (x, y) = current
        if (x, y) in lowest_score:
            current = fringe.pop(0)
            continue
        lowest_score[(x, y)] = score

        for _x, _y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            (x_new, y_new) = (x + _x, y + _y)
            if (
                (x_new, y_new) not in lowest_score
                and (x_new, y_new) not in corrupted
                and x_new >= 0
                and y_new >= 0
                and x_new <= end[0]
                and y_new <= end[1]
            ):
                fringe.append((score + 1, (x_new, y_new)))

        fringe = sorted(set(fringe))
        current = fringe.pop(0)
    return current[0]


print(run(set(corrupted[:1024])))


partial_corruption: Set[Tuple[int, int]] = set()
for pos in corrupted:
    partial_corruption.add(pos)
    try:
        run(partial_corruption)
    except IndexError:
        print(pos)
        break
