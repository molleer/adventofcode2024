from pathlib import Path
from typing import List, Set


disk = [
    x
    for xs in [
        [str(i // 2)] * int(val) if i % 2 == 0 else ["."] * int(val)
        for i, val in enumerate(Path("./input.txt").read_text())
    ]
    for x in xs
]
has_moved: Set[str] = {"."}


def star1():
    def next_space(start=-1, disk=disk):
        for i in range(start + 1, len(disk)):
            if disk[i] == ".":
                return i

        return -1

    def next_file(start=len(disk), disk=disk):
        for i in range(start - 1, 0, -1):
            if disk[i] != ".":
                return i

        return -1

    space_index = next_space()
    file_index = next_file()

    while space_index < file_index and space_index != -1 and file_index != -1:
        (disk[space_index], disk[file_index]) = (disk[file_index], disk[space_index])
        space_index = next_space(space_index)
        file_index = next_file(file_index)

    print(sum([i * int(char) if char != "." else 0 for i, char in enumerate(disk)]))


def star2():
    def move(
        to_start,
        from_start,
        size,
        disk: List[str] = disk,
    ):
        for i in range(size):
            (disk[to_start + i], disk[from_start + i]) = (
                disk[from_start + i],
                disk[to_start + i],
            )

    def next_file(start, disk=disk):
        file_name = ""
        for i in range(start - 1, -1, -1):
            if file_name == "" and disk[i] != ".":
                file_name = disk[i]
                start = i
            if file_name != "" and file_name != disk[i]:
                return (i + 1, start - i)

        if file_name != "":
            return (0, start)

        return (-1, -1)

    def next_space(stop, size, disk=disk):
        stop = min(stop, len(disk))
        for i in range(stop):
            for j in range(size):
                if disk[i + j] != ".":
                    break
            else:
                return i
        return -1

    i = len(disk)

    while True:
        (i, size) = next_file(i)
        if i == -1:
            break
        space_i = next_space(i, size)
        if space_i != -1:
            move(space_i, i, size)

    print(sum([i * int(char) if char != "." else 0 for i, char in enumerate(disk)]))


star2()
