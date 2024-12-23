from pathlib import Path
from typing import Dict, Tuple

nums = [int(n) for n in Path("./input.txt").read_text().split("\n")]


def next_secret(n: int) -> int:
    n = ((n * 64) ^ n) % 16777216
    n = ((n // 32) ^ n) % 16777216
    n = ((n * 2048) ^ n) % 16777216
    return n


sell_prices: Dict[Tuple[int, ...], int] = dict()
sum = 0
for n in nums:
    first_sell_price: Dict[Tuple[int, ...], int] = dict()
    start_range = [0]
    for _ in range(3):
        _n = next_secret(n)
        diff = (_n % 10) - (n % 10)
        start_range.append(diff)
        n = _n

    changes = tuple(start_range)

    for _ in range(1997):
        _n = next_secret(n)
        diff = (_n % 10) - (n % 10)
        changes = tuple([*changes[1:], diff])
        if changes not in first_sell_price:
            first_sell_price[changes] = _n % 10
        n = _n

    for change, price in first_sell_price.items():
        sell_prices[change] = sell_prices.get(change, 0) + price
    sum += n

print(sorted([(price, change) for change, price in sell_prices.items()])[-1])
