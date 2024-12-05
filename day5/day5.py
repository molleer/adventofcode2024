from pathlib import Path

lines = Path("./input.txt").read_text().split("\n")
index = 0

orders = set()

while lines[index] != "":
    orders.add(tuple([int(e) for e in lines[index].split("|")]))
    index += 1

index += 1
updates = []
while index < len(lines):
    updates.append([int(e) for e in lines[index].split(",")])
    index += 1


def follows_order(update, orders=orders):
    passed = set()
    for page in update:
        for other in passed:
            if (page, other) in orders:
                return False

        passed.add(page)
    return True


count = 0
count2 = 0


def bubble_sort(update, orders=orders):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if (update[j], update[i]) in orders:
                tmp = update[j]
                update[j] = update[i]
                update[i] = tmp


for update in updates:
    if follows_order(update):
        # Star 1
        count += update[int(len(update) / 2)]

    else:
        bubble_sort(update)
        count2 += update[int(len(update) / 2)]
print(count2)
