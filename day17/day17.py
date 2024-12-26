from pathlib import Path

lines = Path("./input.txt").read_text().split("\n")
program = [int(x) for x in lines[4][9:].split(",")]

init_registers = [
    int(lines[0][11:]),  # A
    int(lines[1][11:]),  # B
    int(lines[2][11:]),  # C
]


def run(a=init_registers[0], registers=init_registers, program=program):
    registers[0] = a

    def combo(n, registers=registers) -> int:
        if n <= 3:
            return n
        if n <= 6:
            return registers[n - 4]
        raise ValueError()

    output = []
    ip = 0
    while ip < len(program):
        if program[ip] == 0:  # adv
            registers[0] = registers[0] // 2 ** combo(program[ip + 1])
        elif program[ip] == 1:  # bxl
            registers[1] = registers[1] ^ program[ip + 1]
        elif program[ip] == 2:  # bst
            registers[1] = combo(program[ip + 1]) % 8
        elif program[ip] == 3:  # jnz
            if registers[0] != 0:
                ip = program[ip + 1]
                continue
        elif program[ip] == 4:  # bxc
            registers[1] = registers[1] ^ registers[2]
        elif program[ip] == 5:  # out
            output.append(combo(program[ip + 1]) % 8)
        elif program[ip] == 6:  # bdv
            registers[1] = registers[0] // 2 ** combo(program[ip + 1])
        elif program[ip] == 7:  # cdv
            registers[2] = registers[0] // 2 ** combo(program[ip + 1])
        ip += 2
    return ",".join([str(i) for i in output])


def run2(A, start: int):
    B = 0
    program = [2, 4, 1, 3, 7, 5, 4, 2, 0, 3, 1, 5, 5, 5, 3, 0]
    i = len(program) - 1 - start
    while A != 0:
        B = ((A & 0b111) ^ 3) ^ (A >> ((A & 0b111) ^ 3)) ^ 5
        A >>= 3
        if B % 8 != program[i]:
            return i
        i += 1
    return i


def calc(n, i) -> int:
    if i == 16:
        return n
    for j in range(8):
        new_n = (n << 3) + j
        if run2(new_n, i) == 16:
            new_n = calc(new_n, i + 1)
            if new_n != -1:
                return new_n
    return -1


print(run(calc(0, 0)))
