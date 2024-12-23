from pathlib import Path
from typing import Dict, List, Set, Tuple


connections = [line.split("-") for line in Path("./input.txt").read_text().split("\n")]
connects_to: Dict[str, Set[str]] = dict()

for src, dst in connections:
    connects_to.setdefault(src, set()).add(dst)
    connects_to.setdefault(dst, set()).add(src)


def run1():
    groups: Set[Tuple[str, ...]] = set()

    for node in connects_to.keys():
        for c1 in connects_to[node]:
            if node == c1:
                continue
            for c2 in connects_to[c1]:
                if node in connects_to[c2]:
                    groups.add(tuple(sorted([node, c1, c2])))

    groups = set(filter(lambda x: any([name[0] == "t" for name in x]), groups))
    print(len(groups))


def run2():
    def get_qliques(R: Set[str], P: Set[str], X: Set[str]):
        if not P and not X:
            yield R
        while P:
            v = P.pop()
            yield from get_qliques(
                R.union({v}),
                P.intersection(connects_to[v]),
                X.intersection(connects_to[v]),
            )
            X.add(v)

    all_cliques = list(get_qliques(set(), set(connects_to.keys()), set()))
    print(",".join(sorted(sorted(all_cliques, key=lambda x: len(x))[-1])))


run2()
