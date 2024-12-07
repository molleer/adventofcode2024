from pathlib import Path
from itertools import product

lines = Path("./input.txt").read_text().split("\n")
operators = [lambda x, y: x + y, lambda x, y: x * y, lambda x, y: int(str(x) + str(y))]
sum = 0

for line in lines:
    result = int(line.split(":")[0])
    numbers = line.split(": ")[1].split(" ")
    for permutation in product(*[operators for _ in range(len(numbers) - 1)], repeat=1):
        val = int(numbers[0])

        for i, operator in enumerate(permutation):
            val = operator(val, int(numbers[i + 1]))

        if val == result:
            sum += int(result)
            break

print(sum)
