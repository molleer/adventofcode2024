from typing import Dict, Set
from pathlib import Path

lines = Path("./input.txt").read_text().split("\n")
towels = set(lines[0].split(", "))
patterns = lines[2:]
cache: Dict[str, int] = dict()


def fit(pattern: str, towels: Set[str], cache: Dict[str, int] = cache) -> int:
    if pattern in cache:
        return cache[pattern]
    if pattern in towels:
        cache[pattern] = 1
    for i in range(1, len(pattern)):
        if pattern[:i] in towels:
            cache[pattern] = cache.get(pattern, 0) + fit(pattern[i:], towels)
    cache[pattern] = cache.get(pattern, 0)
    return cache[pattern]


count1 = 0
count2 = 0

for pattern in patterns:
    if n := fit(pattern, towels, cache):
        count1 += 1
        count2 += n

print(count1)
print(count2)
