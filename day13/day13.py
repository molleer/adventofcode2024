from pathlib import Path
from typing import Optional, Tuple

blocks = Path("./input.txt").read_text().split("\n\n")
prices = []
parameters = []

for block in blocks:
    if block == "":
        break
    lines = block.split("\n")
    parameters.append(
        (
            int(lines[0].split(",")[0][12:]),
            int(lines[0].split(",")[1][3:]),
            int(lines[1].split(",")[0][12:]),
            int(lines[1].split(",")[1][3:]),
            int(lines[2].split(",")[0][9:]) + 10000000000000,  # Part 2
            int(lines[2].split(",")[1][3:]) + 10000000000000,  # Part 2
        )
    )


def calc(ax, ay, bx, by, x, y) -> Optional[Tuple[int, int]]:
    if (ax * by - ay * bx) == 0:
        return None

    b = (y * ax - x * ay) / (ax * by - ay * bx)
    a = (x - b * bx) / ax

    if a != int(a) or b != int(b) or a < 0 or b < 0:
        return None

    return (int(a), int(b))


sum = 0
for instance in parameters:
    res = calc(*instance)
    if res is None:
        continue
    (a, b) = res
    sum += a * 3 + b

print(sum)
