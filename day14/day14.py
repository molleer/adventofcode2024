from pathlib import Path
from typing import Tuple

steps = 100
height = 103
width = 101

quadrant_count = [0] * 4
lines = Path("./input.txt").read_text().split("\n")
robots = []

for line in lines:
    if line == "":
        break

    p = line.split(" ")[0][2:]
    v = line.split(" ")[1][2:]
    robots.append(
        (
            (
                int(p.split(",")[0]),
                int(p.split(",")[1]),
            ),
            (
                int(v.split(",")[0]),
                int(v.split(",")[1]),
            ),
        )
    )


def step(
    pos,
    vel,
    steps=steps,
    height=height,
    width=width,
) -> Tuple[int, int]:
    return ((pos[0] + vel[0] * steps) % width, (pos[1] + vel[1] * steps) % height)


positions = set([step(*robot, steps=7492) for robot in robots])
for x in range(width):
    line = ""
    for y in range(height):
        if (x, y) in positions:
            line += "*"
        else:
            line += "."
    print(line)
print()

positions = []
for robot in robots:
    (x, y) = step(*robot)
    if x < width // 2:
        if y < height // 2:
            quadrant_count[0] += 1
        elif y > height // 2:
            quadrant_count[1] += 1
    elif x > width // 2:
        if y < height // 2:
            quadrant_count[2] += 1
        elif y > height // 2:
            quadrant_count[3] += 1


print(quadrant_count[0] * quadrant_count[1] * quadrant_count[2] * quadrant_count[3])
