from pathlib import Path
from typing import Dict, List, Set, Tuple

lines = Path("./input.txt").read_text().split("\n")


def get_regions(lines) -> List[Set[Tuple[int, int]]]:
    region_list: List[Set[Tuple[int, int]]] = []
    region_dict: Dict[Tuple[int, int], int] = dict()

    for y, line in enumerate(lines):
        if line == "":
            break
        for x, char in enumerate(line):
            if (x - 1, y) in region_dict and char == lines[y][x - 1]:
                region_list[region_dict[(x - 1, y)]].add((x, y))
                region_dict[(x, y)] = region_dict[(x - 1, y)]
            elif (x, y - 1) in region_dict and char == lines[y - 1][x]:
                region_list[region_dict[(x, y - 1)]].add((x, y))
                region_dict[(x, y)] = region_dict[(x, y - 1)]
            else:
                region_list.append(set([(x, y)]))
                region_dict[(x, y)] = len(region_list) - 1

    def merge(
        pos1: Tuple[int, int],
        pos2: Tuple[int, int],
        region_list: List[Set[Tuple[int, int]]] = region_list,
        region_dict: Dict[Tuple[int, int], int] = region_dict,
    ):
        old_positions = region_list[region_dict[pos2]]
        new_positions = region_list[region_dict[pos1]]
        new_id = region_dict[pos1]

        for pos in old_positions:
            new_positions.add(pos)
            region_dict[pos] = new_id
        old_positions.clear()

    for x, y in region_dict.keys():
        if (
            (x - 1, y) in region_dict
            and region_dict[(x, y)] != region_dict[(x - 1, y)]
            and lines[y][x] == lines[y][x - 1]
        ):
            merge((x - 1, y), (x, y))

        elif (
            (x + 1, y) in region_dict
            and region_dict[(x, y)] != region_dict[(x + 1, y)]
            and lines[y][x] == lines[y][x + 1]
        ):
            merge((x + 1, y), (x, y))

        elif (
            (x, y - 1) in region_dict
            and region_dict[(x, y)] != region_dict[(x, y - 1)]
            and lines[y][x] == lines[y - 1][x]
        ):
            merge((x, y - 1), (x, y))

        elif (
            (x, y + 1) in region_dict
            and region_dict[(x, y)] != region_dict[(x, y + 1)]
            and lines[y][x] == lines[y + 1][x]
        ):
            merge((x, y + 1), (x, y))

    return list(filter(lambda x: len(x) != 0, region_list))


regions = get_regions(lines)
fence_len = [0] * len(regions)
corners = [[] for _ in regions]

for region, positions in enumerate(regions):
    for x, y in positions:
        if (x + 1, y + 1) not in positions and not (
            ((x + 1, y) in positions) ^ ((x, y + 1) in positions)
        ):
            corners[region].append((x + 1, y + 1))
        if (x + 1, y - 1) not in positions and not (
            ((x + 1, y) in positions) ^ ((x, y - 1) in positions)
        ):
            corners[region].append((x + 1, y - 1))
        if (x - 1, y + 1) not in positions and not (
            ((x - 1, y) in positions) ^ ((x, y + 1) in positions)
        ):
            corners[region].append((x - 1, y + 1))
        if (x - 1, y - 1) not in positions and not (
            ((x - 1, y) in positions) ^ ((x, y - 1) in positions)
        ):
            corners[region].append((x - 1, y - 1))

        if (x + 1, y + 1) in positions and not (
            ((x + 1, y) in positions) or ((x, y + 1) in positions)
        ):
            corners[region].append((x + 1, y + 1))
        if (x + 1, y - 1) in positions and not (
            ((x + 1, y) in positions) or ((x, y - 1) in positions)
        ):
            corners[region].append((x + 1, y - 1))
        if (x - 1, y + 1) in positions and not (
            ((x - 1, y) in positions) or ((x, y + 1) in positions)
        ):
            corners[region].append((x - 1, y + 1))
        if (x - 1, y - 1) in positions and not (
            ((x - 1, y) in positions) or ((x, y - 1) in positions)
        ):
            corners[region].append((x - 1, y - 1))


for region, positions in enumerate(regions):
    for pos in positions:
        if (pos[0] + 1, pos[1]) not in positions:
            fence_len[region] += 1
        if (pos[0] - 1, pos[1]) not in positions:
            fence_len[region] += 1
        if (pos[0], pos[1] + 1) not in positions:
            fence_len[region] += 1
        if (pos[0], pos[1] - 1) not in positions:
            fence_len[region] += 1
print(
    "Star 1",
    sum(
        [fence_len[region] * len(positions) for region, positions in enumerate(regions)]
    ),
)

print(
    "Star 2",
    sum(
        [
            len(corners[region]) * len(positions)
            for region, positions in enumerate(regions)
        ]
    ),
)
