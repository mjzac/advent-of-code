# https://adventofcode.com/2019/day/5

program = None

instruction_lengths = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4}


def reset_program():
    with open("5input.txt") as f:
        global program
        program = list(map(int, f.readline().split(",")))


def get_mods(instruction):
    parameter_modes_str = reversed(str(instruction)[:-2])
    parameter_modes = list(map(int, parameter_modes_str))
    while len(parameter_modes) < 4:
        parameter_modes.append(0)
    return parameter_modes


POSITION_MODE = 0


def get_operand(idx, mode):
    if mode == POSITION_MODE:
        return program[program[idx]]
    else:
        return program[idx]


def get_two_operands(ptr):
    modes = get_mods(program[ptr])
    return (get_operand(ptr + 1, modes[0]), get_operand(ptr + 2, modes[1]))


def set_value(idx, val):
    program[idx] = val


def run(input_id=1):
    instruction_ptr = 0
    instruction_ptr_modified = False
    opcode = int(str(program[instruction_ptr])[-2:])
    output_val = None
    while opcode != 99:
        if opcode == 1:
            operand1, operand2 = get_two_operands(instruction_ptr)
            set_value(program[instruction_ptr + 3], operand1 + operand2)
        elif opcode == 2:
            operand1, operand2 = get_two_operands(instruction_ptr)
            set_value(program[instruction_ptr + 3], operand1 * operand2)
        elif opcode == 3:
            set_value(program[instruction_ptr + 1], input_id)
        elif opcode == 4:
            output_val = program[program[instruction_ptr + 1]]
        elif opcode == 5:
            operand1, operand2 = get_two_operands(instruction_ptr)
            if operand1 != 0:
                instruction_ptr = operand2
                instruction_ptr_modified = True

        elif opcode == 6:
            operand1, operand2 = get_two_operands(instruction_ptr)
            if operand1 == 0:
                instruction_ptr = operand2
                instruction_ptr_modified = True
        elif opcode == 7:
            operand1, operand2 = get_two_operands(instruction_ptr)
            result_val = 1 if operand1 < operand2 else 0
            set_value(program[instruction_ptr + 3], result_val)

        elif opcode == 8:
            operand1, operand2 = get_two_operands(instruction_ptr)
            result_val = 1 if operand1 == operand2 else 0
            set_value(program[instruction_ptr + 3], result_val)
        if not instruction_ptr_modified:
            instruction_ptr += instruction_lengths[opcode]
        instruction_ptr_modified = False
        opcode = int(str(program[instruction_ptr])[-2:])

    return output_val


def part_1():
    reset_program()
    return run(input_id=1)


def part_2():
    reset_program()
    return run(input_id=5)


if __name__ == "__main__":
    print(part_2())
