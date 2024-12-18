from pathlib import Path

init_map = Path("./input.txt").read_text().split("\n\n")[0]
init_map = (
    init_map.replace("#", "##").replace(".", "..").replace("@", "@.").replace("O", "[]")
)
moves = Path("./input.txt").read_text().split("\n\n")[1]

map = [list(line) for line in init_map.split("\n")]
robot_pos = (-1, -1)

for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == "@":
            robot_pos = (x, y)
            map[y][x] = "."


def _can_move(pos, dir, map=map) -> bool:
    """[]
    Assumes we are here: ^
    """
    if map[pos[1]][pos[0]] != "[":
        return map[pos[1]][pos[0]] != "#" and map[pos[1]][pos[0] + 1] != "#"
    if map[pos[1] + dir[1]][pos[0]] == "[":
        return _can_move((pos[0], pos[1] + dir[1]), dir, map=map)
    if map[pos[1] + dir[1]][pos[0]] == "]" and not _can_move(
        (pos[0] - 1, pos[1] + dir[1]), dir, map=map
    ):
        return False
    if map[pos[1] + dir[1]][pos[0] + 1] == "[" and not _can_move(
        (pos[0] + 1, pos[1] + dir[1]), dir, map=map
    ):
        return False
    return (
        map[pos[1] + dir[1]][pos[0]] != "#" and map[pos[1] + dir[1]][pos[0] + 1] != "#"
    )


def can_move(pos, dir, map=map) -> bool:
    if dir[1] == 0:
        while map[pos[1]][pos[0]] in ("[", "]"):
            pos = (pos[0] + dir[0], pos[1] + dir[1])
        return map[pos[1]][pos[0]] != "#"

    if map[pos[1]][pos[0]] == "[":
        return _can_move(pos, dir, map)
    elif map[pos[1]][pos[0]] == "]":
        return _can_move((pos[0] - 1, pos[1]), dir, map)

    return map[pos[1]][pos[0]] != "#"


def _move(pos, dir, map=map):
    if map[pos[1] + dir[1]][pos[0]] == "[":
        move((pos[0], pos[1] + dir[1]), dir, map=map)

    if map[pos[1] + dir[1]][pos[0]] == "]":
        move((pos[0] - 1, pos[1] + dir[1]), dir, map=map)

    if map[pos[1] + dir[1]][pos[0] + 1] == "[":
        move((pos[0] + 1, pos[1] + dir[1]), dir, map=map)

    map[pos[1] + dir[1]][pos[0]] = "["
    map[pos[1] + dir[1]][pos[0] + 1] = "]"
    map[pos[1]][pos[0]] = "."
    map[pos[1]][pos[0] + 1] = "."


def move(pos, dir, map=map):
    if dir[1] == 0:
        (x, y) = (pos[0] + dir[0], pos[1])
        if map[y][x] in "[]":
            move((x, y), dir, map=map)

        map[y][x] = map[pos[1]][pos[0]]
        map[pos[1]][pos[0]] = "."
    else:
        if map[pos[1]][pos[0]] == "[":
            _move(pos, dir, map=map)
        else:
            _move((pos[0] - 1, pos[1]), dir, map=map)


actions = {
    "v": (0, 1),
    "^": (0, -1),
    "<": (-1, 0),
    ">": (1, 0),
}


def print_map(robot_pos, map=map):
    for y, row in enumerate(map):
        line = "".join(row)
        if robot_pos[1] == y:
            line = "".join(row[: robot_pos[0]]) + "@" + "".join(row[robot_pos[0] + 1 :])
        print(line)


for action in moves:
    if action == "\n":
        continue
    dir = actions[action]
    new_pos = (robot_pos[0] + dir[0], robot_pos[1] + dir[1])
    if can_move(new_pos, dir):
        if map[new_pos[1]][new_pos[0]] in "[]":
            move(new_pos, dir)
        robot_pos = new_pos
    # print_map(robot_pos)

gps = 0
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == "[":
            gps += 100 * y + x
print(gps)
