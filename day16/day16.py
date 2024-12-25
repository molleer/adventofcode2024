# Implement A*

from typing import Dict, List, Set, Tuple
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


def start1(map=map):
    end = find_e()
    start = find_s()
    fringe = [(0, start, (1, 0))]
    lowest_score: Dict[Tuple[Tuple[int, int], Tuple[int, int]], int] = dict()
    current: Tuple[int, Tuple[int, int], Tuple[int, int]] = fringe.pop()

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

    return current[0]


score = start1()
n_steps = score % 1000
n_turns = (score - n_steps) // 1000
print(n_steps, n_turns)


def bfs(steps: int, turns: int, map=map):
    start = find_s(map)
    end = find_e(map)
    new_fringe: List[
        Tuple[Tuple[int, int], Tuple[int, int], int, Tuple[Tuple[int, int], ...]]
    ] = [(start, (1, 0), turns, (start,))]
    fringe: List[
        Tuple[Tuple[int, int], Tuple[int, int], int, Tuple[Tuple[int, int], ...]]
    ] = []  # pos, steps left, turns left
    visited = set()

    for step in range(steps - 1):
        paths: Dict[
            Tuple[Tuple[int, int], Tuple[int, int], int],
            Tuple[Tuple[int, int], ...],
        ] = dict()
        for p in new_fringe:
            s: Set[Tuple[int, int]] = set()
            s.update(paths.get((p[0], p[1], p[2]), tuple()))
            s.update(p[3])
            paths[(p[0], p[1], p[2])] = tuple(s)

        fringe = []
        for key, val in paths.items():
            fringe.append((*key, val))

        new_fringe = []

        for current in fringe:
            (x, y), (x_dir, y_dir), turns_left, path = current
            if (x, y) == end and turns_left > 0:
                continue
            else:
                visited.add(((x, y), turns_left))

            (x_dir_new, y_dir_new) = (x_dir, y_dir)
            (x_new, y_new) = (x + x_dir_new, y + y_dir_new)
            if ((x_new, y_new), turns_left) not in visited and map[y_new][x_new] != "#":
                new_fringe.append(
                    (
                        (x_new, y_new),
                        (x_dir_new, y_dir_new),
                        turns_left,
                        (*path, (x_new, y_new)),
                    )
                )

            if turns_left == 0:
                continue

            # Left turn
            (x_dir_new, y_dir_new) = (y_dir, -x_dir)
            (x_new, y_new) = (x + x_dir_new, y + y_dir_new)
            if ((x_new, y_new), turns_left - 1) not in visited and map[y_new][
                x_new
            ] != "#":
                new_fringe.append(
                    (
                        (x_new, y_new),
                        (x_dir_new, y_dir_new),
                        turns_left - 1,
                        (*path, (x_new, y_new)),
                    )
                )

            # Right turn
            (x_dir_new, y_dir_new) = (-y_dir, x_dir)
            (x_new, y_new) = (x + x_dir_new, y + y_dir_new)
            if ((x_new, y_new), turns_left - 1) not in visited and map[y_new][
                x_new
            ] != "#":
                new_fringe.append(
                    (
                        (x_new, y_new),
                        (x_dir_new, y_dir_new),
                        turns_left - 1,
                        (*path, (x_new, y_new)),
                    )
                )

    end_neighbours = [
        (end[0] + 1, end[1]),
        (end[0] - 1, end[1]),
        (end[0], end[1] + 1),
        (end[0], end[1] - 1),
    ]

    fringe = [path for path in new_fringe if path[0] in end_neighbours]
    positions: Set[Tuple[int, int]] = set([end])
    for p in fringe:
        positions.update(p[3])
    print(len(positions))


bfs(n_steps, n_turns)
