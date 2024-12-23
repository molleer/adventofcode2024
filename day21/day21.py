from typing import List, Tuple
from pathlib import Path

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


def coords_to_arrows(coords: List[Tuple[int, int]], num_pad=False) -> str:
    arrows = ""
    current = coords.pop(0)
    for c in coords:
        x_part = ""
        y_part = ""
        x_diff = current[0] - c[0]
        y_diff = current[1] - c[1]
        if x_diff > 0:
            x_part += "<" * x_diff
        if x_diff < 0:
            x_part += ">" * (-x_diff)
        if y_diff > 0:
            y_part += "^" * y_diff
        if y_diff < 0:
            y_part += "v" * (-y_diff)

        if current[0] == 0:
            arrows += x_part + y_part
        elif num_pad and current[1] == 3:
            arrows += y_part + x_part
        elif not num_pad and current[1] == 0:
            arrows += y_part + x_part
        else:
            arrows += x_part + y_part

        current = c
        arrows += "A"
    return arrows


def translate1(line: str) -> str:
    arrows = coords_to_arrows(num_to_coords(line), num_pad=True)
    for _ in range(2):
        arrows = coords_to_arrows(arrows_to_coords(arrows))
    return arrows


sum = 0
for line in lines:
    orders = translate1(line)
    num = int("".join(filter(lambda x: x in "0123456789", line)))
    sum += num * len(orders)

print(sum)
