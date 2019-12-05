# https://adventofcode.com/2019/day/5

program = None

instruction_lengths = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4}


def reset_program():
    with open("5input.txt") as f:
        global program
        program = list(map(int, f.readline().split(",")))


def run(is_part2=False):
    instruction_ptr = 0
    instruction_ptr_modified = False
    opcode = int(str(program[instruction_ptr])[-2:])
    while opcode != 99:
        parameter_mode = reversed(str(program[instruction_ptr])[:-2])
        parameter_modes = list(map(int, parameter_mode))
        while len(parameter_modes) < 4:
            parameter_modes.append(0)
        if opcode == 1:
            operand1_idx = program[instruction_ptr + 1]
            operand2_idx = program[instruction_ptr + 2]
            result_idx = program[instruction_ptr + 3]
            operand1 = (
                program[operand1_idx] if parameter_modes[0] == 0 else operand1_idx
            )

            operand2 = (
                program[operand2_idx] if parameter_modes[1] == 0 else operand2_idx
            )
            program[result_idx] = operand1 + operand2
        elif opcode == 2:
            operand1_idx = program[instruction_ptr + 1]
            operand2_idx = program[instruction_ptr + 2]
            result_idx = program[instruction_ptr + 3]
            operand1 = (
                program[operand1_idx] if parameter_modes[0] == 0 else operand1_idx
            )
            operand2 = (
                program[operand2_idx] if parameter_modes[1] == 0 else operand2_idx
            )
            program[result_idx] = operand1 * operand2

        elif opcode == 3:
            if is_part2:
                input_id = 5
            else:
                input_id = 1
            program[program[instruction_ptr + 1]] = input_id
        elif opcode == 4:
            ptr_increment = 2
            print(program[program[instruction_ptr + 1]])
        elif is_part2 and opcode == 5:
            operand1_idx = program[instruction_ptr + 1]
            if parameter_modes[0] == 0:
                operand1 = program[operand1_idx]
            else:
                operand1 = operand1_idx

            operand2_idx = program[instruction_ptr + 2]
            if parameter_modes[1] == 0:
                operand2 = program[operand2_idx]
            else:
                operand2 = operand2_idx
            if operand1 != 0:
                instruction_ptr = operand2
                instruction_ptr_modified = True

        elif is_part2 and opcode == 6:
            operand1_idx = program[instruction_ptr + 1]
            if parameter_modes[0] == 0:
                operand1 = program[operand1_idx]
            else:
                operand1 = operand1_idx

            operand2_idx = program[instruction_ptr + 2]
            if parameter_modes[1] == 0:
                operand2 = program[operand2_idx]
            else:
                operand2 = operand2_idx
            if operand1 == 0:
                instruction_ptr = operand2
                instruction_ptr_modified = True
        elif is_part2 and opcode == 7:
            operand1_idx = program[instruction_ptr + 1]
            if parameter_modes[0] == 0:
                operand1 = program[operand1_idx]
            else:
                operand1 = operand1_idx

            operand2_idx = program[instruction_ptr + 2]
            if parameter_modes[1] == 0:
                operand2 = program[operand2_idx]
            else:
                operand2 = operand2_idx

            if operand1 < operand2:
                result_val = 1
            else:
                result_val = 0
            program[program[instruction_ptr + 3]] = result_val

        elif is_part2 and opcode == 8:
            operand1_idx = program[instruction_ptr + 1]
            if parameter_modes[0] == 0:
                operand1 = program[operand1_idx]
            else:
                operand1 = operand1_idx

            operand2_idx = program[instruction_ptr + 2]
            if parameter_modes[1] == 0:
                operand2 = program[operand2_idx]
            else:
                operand2 = operand2_idx

            if operand1 == operand2:
                result_val = 1
            else:
                result_val = 0
            program[program[instruction_ptr + 3]] = result_val
        if not instruction_ptr_modified:
            instruction_ptr += instruction_lengths[opcode]
        instruction_ptr_modified = False
        opcode = int(str(program[instruction_ptr])[-2:])

    return program[0]


def part_1():
    reset_program()
    return run()


def part_2():
    reset_program()
    return run(is_part2=True)


if __name__ == "__main__":
    part_2()
