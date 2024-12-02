from pathlib import Path
from typing import List


def decreasing(
    report: List[int],
    bad: int = 0,
) -> bool:
    if bad < 0:
        return False
    for i in range(len(report) - 1):
        diff = report[i] - report[i + 1]
        if diff <= 0 or diff > 3:
            return decreasing(report[:i] + report[i + 1 :], bad - 1) or decreasing(
                report[: i + 1] + report[i + 2 :], bad - 1
            )
    return True


def increasing(
    report: List[int],
    bad: int = 0,
) -> bool:
    if bad < 0:
        return False
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if diff <= 0 or diff > 3:
            return increasing(report[:i] + report[i + 1 :], bad - 1) or increasing(
                report[: i + 1] + report[i + 2 :], bad - 1
            )
    return True


def star1():
    reports = [
        [int(i) for i in line.split(" ")]
        for line in Path("./input.txt").read_text().split("\n")
    ]
    count = 0

    for report in reports:
        if decreasing(report):
            count += 1
        if increasing(report):
            count += 1

    print(count)


def star2():
    reports = [
        [int(i) for i in line.split(" ")]
        for line in Path("./input.txt").read_text().split("\n")
    ]
    count = 0

    for report in reports:
        if decreasing(report, bad=1):
            count += 1
        elif increasing(report, bad=1):
            count += 1

    print(count)


star2()
