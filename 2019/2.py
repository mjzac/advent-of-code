program = None


def reset_program():
    with open("2input.txt") as f:
        global program
        program = list(map(int, f.readline().split(",")))


def run():
    opcode_position = 0
    operand1_position = 1
    operand2_position = 2
    result_position = 3

    opcode = program[opcode_position]
    while opcode != 99:
        if opcode == 1:
            program[program[result_position]] = (
                program[program[operand1_position]]
                + program[program[operand2_position]]
            )
        elif opcode == 2:
            program[program[result_position]] = (
                program[program[operand1_position]]
                * program[program[operand2_position]]
            )
        opcode_position += 4
        operand1_position += 4
        operand2_position += 4
        result_position += 4
        opcode = program[opcode_position]
    return program[0]


def part_1():
    reset_program()
    program[1] = 12
    program[2] = 2


if __name__ == "__main__":
    print(part_1)
