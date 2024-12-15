from pathlib import Path

init_map = Path("./input.txt").read_text().split("\n\n")[0]
moves = Path("./input.txt").read_text().split("\n\n")[1]

map = [list(line) for line in init_map.split("\n")]
robot_pos = (-1, -1)

for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == "@":
            robot_pos = (x, y)
            map[y][x] = "."


def can_move(pos, dir, map=map) -> bool:
    while map[pos[1]][pos[0]] == "O":
        pos = (pos[0] + dir[0], pos[1] + dir[1])

    return map[pos[1]][pos[0]] != "#"


def move(pos, dir, map=map):
    (x, y) = (pos[0] + dir[0], pos[1] + dir[1])
    if map[y][x] == "O":
        move((x, y), dir, map=map)

    map[pos[1]][pos[0]] = "."
    map[y][x] = "O"


actions = {
    "v": (0, 1),
    "^": (0, -1),
    "<": (-1, 0),
    ">": (1, 0),
}


for action in moves:
    if action == "\n":
        continue

    dir = actions[action]
    new_pos = (robot_pos[0] + dir[0], robot_pos[1] + dir[1])
    if can_move(new_pos, dir):
        if map[new_pos[1]][new_pos[0]] == "O":
            move(new_pos, dir)
        robot_pos = new_pos

gps = 0
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == "O":
            gps += 100 * y + x

print(gps)
