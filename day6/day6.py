from pathlib import Path
from typing import Set, Tuple


def star1():
    direction = (0, -1)
    distinct_positions: Set[Tuple[Tuple[int, int], Tuple[int, int]]] = set()

    lab = Path("./input.txt").read_text().split()

    def get_guard(lab=lab):
        for y, line in enumerate(lab):
            for x, char in enumerate(line):
                if char == "^":
                    return (x, y)
        raise Exception("Guard not found!")

    pos = get_guard()
    distinct_positions.add((pos, direction))

    while True:
        next_y = pos[1] + direction[1]
        next_x = pos[0] + direction[0]

        if next_y >= len(lab) or next_y < 0 or next_x >= len(lab[next_y]) or next_x < 0:
            break

        if lab[next_y][next_x] == "#":
            direction = (-direction[1], direction[0])
            continue

        pos = (next_x, next_y)
        if (pos, direction) in distinct_positions:
            break

        distinct_positions.add((pos, direction))

    positions = {p for p, _ in distinct_positions}
    print(len(positions))


def star2():
    direction = (0, -1)

    lab = Path("./input.txt").read_text().split()

    def get_guard(lab=lab):
        for y, line in enumerate(lab):
            for x, char in enumerate(line):
                if char == "^":
                    return (x, y)
        raise Exception("Guard not found!")

    pos = get_guard()

    def walk(pos, dir, lab=lab, extra_blocker=None) -> bool:
        distinct_positions: Set[Tuple[Tuple[int, int], Tuple[int, int]]] = set()
        obsticles: Set[Tuple[int, int]] = set()

        while True:
            if (pos, dir) in distinct_positions:
                return True

            distinct_positions.add((pos, dir))

            next_y = pos[1] + dir[1]
            next_x = pos[0] + dir[0]

            if (
                next_y >= len(lab)
                or next_y < 0
                or next_x >= len(lab[next_y])
                or next_x < 0
            ):
                if extra_blocker is None:
                    print("blockers: ", len(obsticles))
                return False

            if lab[next_y][next_x] == "#" or (next_x, next_y) == extra_blocker:
                dir = (-dir[1], dir[0])
                continue

            if extra_blocker is None and (next_x, next_y) not in {
                p for p, _ in distinct_positions
            }:
                looped = walk(pos, (-dir[1], dir[0]), extra_blocker=(next_x, next_y))
                if looped:
                    obsticles.add((next_x, next_y))

            pos = (next_x, next_y)

    walk(pos, direction)


star2()
