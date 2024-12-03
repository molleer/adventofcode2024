import re
from pathlib import Path

mul = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
sum = 0

dont = r"don't\(\)"
_do = r"do\(\)"

enabled = True

for line in Path("./input.txt").read_text().split("\n"):
    donts = [(match.start(), "dont") for match in re.finditer(re.compile(dont), line)]
    dos = [(match.start(), "do") for match in re.finditer(re.compile(_do), line)]
    matches = [
        (match.start(), match.group()) for match in re.finditer(re.compile(mul), line)
    ]

    for index, name in sorted([*donts, *dos, *matches]):
        if name == "do":
            enabled = True
            continue
        if name == "dont":
            enabled = False
            continue

        if not enabled:
            continue

        first = int(name.split(",")[0].removeprefix("mul("))
        second = int(name.split(",")[1].removesuffix(")"))
        sum += first * second

print(sum)
