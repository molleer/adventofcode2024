from pathlib import Path

blocks = Path("./input.txt").read_text().split("\n\n")
locks = [block for block in blocks if block.startswith("#####")]
keys = [block for block in blocks if block.endswith("#####")]

lock_cols = []
for lock in locks:
    lines = lock.split("\n")
    cols = [0] * len(lines[0])
    for i in range(1, len(lines)):
        for col, val in enumerate(lines[i]):
            if val == "#":
                cols[col] += 1
    lock_cols.append(cols)

key_cols = []
for key in keys:
    lines = key.split("\n")
    cols = [0] * len(lines[0])
    for i in range(len(lines) - 2, -1, -1):
        for col, val in enumerate(lines[i]):
            if val == "#":
                cols[col] += 1
    key_cols.append(cols)

fit_count = 0
for _key in key_cols:
    for _lock in lock_cols:
        if all([v < 6 for v in map(sum, zip(_key, _lock))]):
            fit_count += 1

print(fit_count)
