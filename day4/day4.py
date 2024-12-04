import re
from pathlib import Path
from typing import List, Tuple

lines = Path("./input.txt").read_text().split("\n")
count = 0


def star1():
    WORD = "XMAS"

    # horrisontal
    for line in lines:
        matches = re.findall(re.compile(WORD), line)
        if matches:
            count += len(matches)

    # horrisontal
    for line in lines:
        matches = re.findall(re.compile("".join(reversed("MAS"))), line)
        if matches:
            count += len(matches)

    # vertical
    sub_strings: List[Tuple[int, int]] = []
    for line in lines:
        new_sub_strings: List[Tuple[int, int]] = []
        for length, x in sub_strings:
            if line[x] == WORD[length]:
                if length + 1 == len(WORD):
                    count += 1
                else:
                    new_sub_strings.append((length + 1, x))

        for x in range(len(line)):
            if line[x] == WORD[0]:
                new_sub_strings.append((1, x))

        sub_strings = new_sub_strings

    # vertical 2
    sub_strings = []
    for line in reversed(lines):
        new_sub_strings = []
        for length, x in sub_strings:
            if line[x] == WORD[length]:
                if length + 1 == len(WORD):
                    count += 1
                else:
                    new_sub_strings.append((length + 1, x))

        for x in range(len(line)):
            if line[x] == WORD[0]:
                new_sub_strings.append((1, x))

        sub_strings = new_sub_strings

    # diag 1
    sub_strings = []
    for line in lines:
        new_sub_strings = []
        for length, x in sub_strings:
            if x < len(line) and line[x] == WORD[length]:
                if length + 1 == len(WORD):
                    count += 1
                else:
                    new_sub_strings.append((length + 1, x + 1))

        for x in range(len(line)):
            if line[x] == WORD[0]:
                new_sub_strings.append((1, x + 1))

        sub_strings = new_sub_strings

    # diag 1.2
    sub_strings = []
    for line in reversed(lines):
        new_sub_strings = []
        for length, x in sub_strings:
            if x < len(line) and line[x] == WORD[length]:
                if length + 1 == len(WORD):
                    count += 1
                else:
                    new_sub_strings.append((length + 1, x + 1))

        for x in range(len(line)):
            if line[x] == WORD[0]:
                new_sub_strings.append((1, x + 1))

        sub_strings = new_sub_strings

    # diag 2
    sub_strings = []
    for line in lines:
        new_sub_strings = []
        for length, x in sub_strings:
            if x >= 0 and line[x] == WORD[length]:
                if length + 1 == len(WORD):
                    count += 1
                else:
                    new_sub_strings.append((length + 1, x - 1))

        for x in range(len(line)):
            if line[x] == WORD[0]:
                new_sub_strings.append((1, x - 1))

        sub_strings = new_sub_strings

    # diag 2.1
    sub_strings = []
    for line in reversed(lines):
        new_sub_strings = []
        for length, x in sub_strings:
            if x >= 0 and line[x] == WORD[length]:
                if length + 1 == len(WORD):
                    count += 1
                else:
                    new_sub_strings.append((length + 1, x - 1))

        for x in range(len(line)):
            if line[x] == WORD[0]:
                new_sub_strings.append((1, x - 1))

        sub_strings = new_sub_strings


def star2():
    WORD = "MAS"
    count = 0
    centers = []

    # diag 1
    sub_strings = []
    for y, line in enumerate(lines):
        new_sub_strings = []
        for length, x in sub_strings:
            if x < len(line) and line[x] == WORD[length]:
                if length + 1 == len(WORD):
                    center = (x - 1, y - 1)
                    if center in centers:
                        count += 1
                        centers.remove(center)
                    else:
                        centers += [center]
                else:
                    new_sub_strings.append((length + 1, x + 1))

        for x in range(len(line)):
            if line[x] == WORD[0]:
                new_sub_strings.append((1, x + 1))

        sub_strings = new_sub_strings

    print(centers)

    # diag 1.2
    sub_strings = []
    for y, line in enumerate(reversed(lines)):
        new_sub_strings = []
        for length, x in sub_strings:
            if x < len(line) and line[x] == WORD[length]:
                if length + 1 == len(WORD):
                    center = (x - 1, len(lines) - y)
                    if center in centers:
                        count += 1
                        centers.remove(center)
                    else:
                        centers += [center]
                else:
                    new_sub_strings.append((length + 1, x + 1))

        for x in range(len(line)):
            if line[x] == WORD[0]:
                new_sub_strings.append((1, x + 1))

        sub_strings = new_sub_strings

    print(centers)

    # diag 2
    sub_strings = []
    for y, line in enumerate(lines):
        new_sub_strings = []
        for length, x in sub_strings:
            if x >= 0 and line[x] == WORD[length]:
                if length + 1 == len(WORD):
                    center = (x + 1, y - 1)
                    if center in centers:
                        count += 1
                        centers.remove(center)
                    else:
                        centers += [center]
                else:
                    new_sub_strings.append((length + 1, x - 1))

        for x in range(len(line)):
            if line[x] == WORD[0]:
                new_sub_strings.append((1, x - 1))

        sub_strings = new_sub_strings
    print(centers)
    # diag 2
    sub_strings = []
    for y, line in enumerate(reversed(lines)):
        new_sub_strings = []
        for length, x in sub_strings:
            if x >= 0 and line[x] == WORD[length]:
                if length + 1 == len(WORD):
                    center = (x + 1, len(lines) - y)
                    if center in centers:
                        count += 1
                        centers.remove(center)
                    else:
                        centers += [center]
                else:
                    new_sub_strings.append((length + 1, x - 1))

        for x in range(len(line)):
            if line[x] == WORD[0]:
                new_sub_strings.append((1, x - 1))

        sub_strings = new_sub_strings
    print(centers)
    print(count)


star2()
