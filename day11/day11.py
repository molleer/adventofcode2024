from typing import Dict, Tuple

steps = 75
stone_list = "2701 64945 0 9959979 93 781524 620 1".split(" ")
stones = list(zip(stone_list, [steps] * len(stone_list)))
cache: Dict[Tuple[str, int], int] = dict()


def blink(stone: Tuple[str, int], cache=cache):
    if stone[1] == 0:
        return 1

    if stone in cache:
        return cache[stone]

    if stone[0] == "0":
        new_stone = ("1", stone[1] - 1)
        res = blink(new_stone, cache)
        cache[new_stone] = res
        return res
    elif len(stone[0]) % 2 == 0:
        new_stone = (str(int(stone[0][: len(stone[0]) // 2])), stone[1] - 1)
        res = blink(new_stone, cache)
        cache[new_stone] = res
        new_stone = (str(int(stone[0][len(stone[0]) // 2 :])), stone[1] - 1)
        res2 = blink(new_stone, cache)
        cache[new_stone] = res2
        return res + res2
    else:
        new_stone = (str(int(stone[0]) * 2024), stone[1] - 1)
        res = blink(new_stone, cache)
        cache[new_stone] = res
        return res


print(sum([blink(stone) for stone in stones]))
