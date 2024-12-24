from pathlib import Path
from typing import Dict, List

GATES = {
    "XOR": lambda a, b: a ^ b,
    "OR": lambda a, b: a or b,
    "AND": lambda a, b: a and b,
}

init_values = [
    line.split(": ")
    for line in Path("./input.txt").read_text().split("\n\n")[0].split("\n")
]
expressions = [
    line.split(" ")
    for line in Path("./input.txt").read_text().split("\n\n")[1].split("\n")
]

values = {name: value == "1" for name, value in init_values}
counts = {
    i: sum([expr[0] in values, expr[2] in values]) for i, expr in enumerate(expressions)
}
fringe = {i for i, _ in enumerate(expressions) if counts[i] == 2}
value_used: Dict[str, List[int]] = dict()
for i, expr in enumerate(expressions):
    value_used.setdefault(expr[0], []).append(i)
    value_used.setdefault(expr[2], []).append(i)

while len(fringe) != 0:
    expr_i = fringe.pop()
    (a, op, b, _, y) = expressions[expr_i]
    output = GATES[op](values[a], values[b])
    values[y] = output

    for next_i in value_used.get(y, []):
        counts[next_i] += 1
        if counts[next_i] == 2:
            fringe.add(next_i)

print(
    "".join(
        [
            "1" if values[key] else "0"
            for key in sorted(
                filter(lambda a: a[0] == "z", values.keys()), reverse=True
            )
        ]
    )
)
