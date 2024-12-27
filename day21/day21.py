from typing import Dict, List, Tuple
from pathlib import Path
from itertools import permutations

lines = Path("./input.txt").read_text().split("\n")

num_pad_coords = {
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "0": (1, 3),
    "A": (2, 3),
}
arrow_coords = {
    "^": (1, 0),
    "A": (2, 0),
    "<": (0, 1),
    "v": (1, 1),
    ">": (2, 1),
}


def num_to_coords(nums: str, num_pad_coords=num_pad_coords) -> List[Tuple[int, int]]:
    return [num_pad_coords["A"]] + [num_pad_coords[n] for n in nums]


def arrows_to_coords(arrows: str, arrow_coords=arrow_coords) -> List[Tuple[int, int]]:
    return [arrow_coords["A"]] + [arrow_coords[n] for n in arrows]


def pass_illegal(pos, path, illegal: List[Tuple[int, int]]) -> bool:
    if pos in illegal:
        return True
    if path == "":
        return False

    if path[0] == "<":
        return pass_illegal((pos[0] - 1, pos[1]), path[1:], illegal)
    if path[0] == ">":
        return pass_illegal((pos[0] + 1, pos[1]), path[1:], illegal)
    if path[0] == "v":
        return pass_illegal((pos[0], pos[1] + 1), path[1:], illegal)
    if path[0] == "^":
        return pass_illegal((pos[0], pos[1] - 1), path[1:], illegal)

    raise ValueError(path[0])


def get_small_paths(
    coords: Dict[str, Tuple[int, int]],
    illegal: List[Tuple[int, int]],
) -> Dict[Tuple[Tuple[int, int], Tuple[int, int]], List[str]]:
    small_paths = dict()
    for c1 in coords.values():
        for c2 in coords.values():
            path = ""
            x_diff = c1[0] - c2[0]
            y_diff = c1[1] - c2[1]
            if x_diff > 0:
                path += "<" * x_diff
            if x_diff < 0:
                path += ">" * (-x_diff)
            if y_diff > 0:
                path += "^" * y_diff
            if y_diff < 0:
                path += "v" * (-y_diff)

            small_paths[(c1, c2)] = [
                "".join(p)
                for p in permutations(path)
                if not pass_illegal(c1, "".join(p), illegal)
            ]

    return small_paths


arrows_small_paths = get_small_paths(arrow_coords, illegal=[(0, 0)])
num_pad_small_paths = get_small_paths(num_pad_coords, illegal=[(0, 3)])


def coords_to_arrows(coords: List[Tuple[int, int]], num_pad=False) -> List[str]:
    paths = set([""])
    small_paths = num_pad_small_paths if num_pad else arrows_small_paths
    current = coords.pop(0)
    for c in coords:
        new_paths = set()
        for p in small_paths[(current, c)]:
            for p2 in paths:
                new_paths.add(p2 + p + "A")
        paths = new_paths
        current = c

    return list(paths)


def arrows_executor(line: str) -> str:
    pos = [2, 0]
    output = ""
    BUTTONS: Dict[Tuple[int, ...], str] = {
        (1, 0): "^",
        (2, 0): "A",
        (0, 1): "<",
        (1, 1): "v",
        (2, 1): ">",
    }
    for char in line:
        if char == "A":
            output += BUTTONS[tuple(pos)]
        elif char == ">":
            pos[0] += 1
        elif char == "<":
            pos[0] -= 1
        elif char == "v":
            pos[1] += 1
        elif char == "^":
            pos[1] -= 1
        else:
            raise ValueError(char)
        assert pos != [0, 0], "Panic!"
    return output


def num_executor(line: str) -> str:
    pos = [2, 3]
    output = ""
    BUTTONS: Dict[Tuple[int, ...], str] = {
        (0, 0): "7",
        (1, 0): "8",
        (2, 0): "9",
        (0, 1): "4",
        (1, 1): "5",
        (2, 1): "6",
        (0, 2): "1",
        (1, 2): "2",
        (2, 2): "3",
        (1, 3): "0",
        (2, 3): "A",
    }
    for char in line:
        if char == "A":
            output += BUTTONS[tuple(pos)]
        elif char == ">":
            pos[0] += 1
        elif char == "<":
            pos[0] -= 1
        elif char == "v":
            pos[1] += 1
        elif char == "^":
            pos[1] -= 1
        else:
            raise ValueError(char)
        assert pos != [0, 3], "Panic!"
    return output


def translate1(code: str):
    paths = coords_to_arrows(num_to_coords(code), num_pad=True)
    for i in range(2):
        new_paths = set()
        for path in paths:
            new_paths.update(coords_to_arrows(arrows_to_coords(path)))
        min_path = min(*[len(p) for p in new_paths])
        paths = list([p for p in new_paths if len(p) == min_path])
        print(len(paths))
    return paths


sum = 0
for line in lines:
    min_arrows = min(*[len(p) for p in translate1(line)])
    num = int("".join(filter(lambda x: x in "0123456789", line)))
    print(num, min_arrows)
    sum += num * min_arrows

print(sum)
