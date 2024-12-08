from pathlib import Path
from typing import Dict, List, Tuple


map = Path("./input.txt").read_text().split("\n")
width = len(map[0])
antennas: Dict[str, List[Tuple[int, int]]] = dict()

for y, line in enumerate(map):
    for x, char in enumerate(line):
        if char != ".":
            if char not in antennas:
                antennas[char] = []
            antennas[char].append((x, y))


def in_map(pos, map=map, width=width) -> bool:
    return pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(map) and pos[1] < width


def get_antinodes(pos, offset):
    antinodes = set()
    while in_map(pos):
        antinodes.add(pos)
        pos = (pos[0] + offset[0], pos[1] + offset[1])
    return antinodes


antinodes = set()
for antenna, locations in antennas.items():
    for k in range(len(locations)):
        for h in range(k + 1, len(locations)):
            pos1 = locations[h]
            pos2 = locations[k]
            antinodes |= get_antinodes(pos1, (pos1[0] - pos2[0], pos1[1] - pos2[1]))
            antinodes |= get_antinodes(pos2, (pos2[0] - pos1[0], pos2[1] - pos1[1]))


print(len(antinodes))
