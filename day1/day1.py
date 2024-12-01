from pathlib import Path

def star1():
    lines = Path("./input.txt").read_text().split("\n")
    first = []
    second = []

    for line in lines:
        (a,b) = line.split("   ")
        first.append(int(a))
        second.append(int(b))

    sum = 0
    for a, b in zip(sorted(first), sorted(second)):
        sum += abs(a - b)

    print(sum)

def star2():
    lines = Path("./input.txt").read_text().split("\n")
    first = []
    second = dict()

    for line in lines:
        (a,b) = line.split("   ")
        
        first.append(int(a))
        second[int(b)] = second.get(int(b), 0) + 1

    sum = 0
    for num in first:
        times = second.get(num, 0)
        sum += times * num

    print(sum)

star2()