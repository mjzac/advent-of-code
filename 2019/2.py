# https://adventofcode.com/2019/day/2

program = None


def reset_program():
    with open("2input.txt") as f:
        global program
        program = list(map(int, f.readline().split(",")))


def run():
    opcode_idx = 0
    operand1_idx = 1
    operand2_idx = 2
    result_idx = 3

    opcode = program[opcode_idx]

    while opcode != 99:
        if opcode == 1:
            program[program[result_idx]] = (
                program[program[operand1_idx]] + program[program[operand2_idx]]
            )
        elif opcode == 2:
            program[program[result_idx]] = (
                program[program[operand1_idx]] * program[program[operand2_idx]]
            )
        opcode_idx += 4
        operand1_idx += 4
        operand2_idx += 4
        result_idx += 4
        opcode = program[opcode_idx]
    return program[0]


def part_1():
    reset_program()
    program[1] = 12
    program[2] = 2
    return run()


def part_2():
    for noun in range(100):
        for verb in range(100):
            reset_program()
            program[1] = noun
            program[2] = verb
            output = run()
            if output == 19690720:
                return noun * 100 + verb


if __name__ == "__main__":
    print(part_2())
