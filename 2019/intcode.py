class Intcode(object):
    def __init__(self, program, ip_seq=[]):
        self.instruction_ptr = 0
        self.program = program
        self.mode = [0] * 4
        self.ip_seq = ip_seq
        self.op = None
        self.halted = False
        super().__init__()

    def add_ip(self, ip_val):
        self.ip_seq.append(ip_val)

    def get_mods(self):
        parameter_modes_str = reversed(str(self.program[self.instruction_ptr])[:-2])
        parameter_modes = list(map(int, parameter_modes_str))
        while len(parameter_modes) < 4:
            parameter_modes.append(0)
        self.mode = parameter_modes

    def get_next_cmd(self):
        return int(str(self.program[self.instruction_ptr])[-2:])

    def move(self, offset):
        self.instruction_ptr += offset

    def set_value(self, idx, val):
        self.program[idx] = val

    def get_operand(self, idx, mode):
        POSITION_MODE = 0
        if mode == POSITION_MODE:
            return self.program[self.program[idx]]
        else:
            return self.program[idx]

    def get_two_operands(self):
        self.get_mods()
        return (
            self.get_operand(self.instruction_ptr + 1, self.mode[0]),
            self.get_operand(self.instruction_ptr + 2, self.mode[1]),
        )

    def add(self, op1, op2):
        self.set_value(self.program[self.instruction_ptr + 3], op1 + op2)
        self.move(4)

    def multiply(self, op1, op2):
        self.set_value(self.program[self.instruction_ptr + 3], op1 * op2)
        self.move(4)

    def get_ip(self):
        self.set_value(self.program[self.instruction_ptr + 1], self.ip_seq.pop(0))
        self.move(2)

    def get_op(self):
        self.op = self.program[self.program[self.instruction_ptr + 1]]
        self.move(2)

    def jump_true(self, op1, op2):
        if op1 != 0:
            self.instruction_ptr = op2
        else:
            self.move(3)

    def jump_false(self, op1, op2):
        if op1 == 0:
            self.instruction_ptr = op2
        else:
            self.move(3)

    def less_than(self, op1, op2):
        result_val = 1 if op1 < op2 else 0
        self.set_value(self.program[self.instruction_ptr + 3], result_val)
        self.move(4)

    def equals(self, op1, op2):
        result_val = 1 if op1 == op2 else 0
        self.set_value(self.program[self.instruction_ptr + 3], result_val)
        self.move(4)

    def execute(self, feedback_mode=False):
        mapping = {
            1: lambda: self.add(*self.get_two_operands()),
            2: lambda: self.multiply(*self.get_two_operands()),
            3: lambda: self.get_ip(),
            4: lambda: self.get_op(),
            5: lambda: self.jump_true(*self.get_two_operands()),
            6: lambda: self.jump_false(*self.get_two_operands()),
            7: lambda: self.less_than(*self.get_two_operands()),
            8: lambda: self.equals(*self.get_two_operands()),
        }
        cmd = self.get_next_cmd()
        while cmd != 99:
            mapping[cmd]()
            if cmd == 4 and feedback_mode:
                return self.op
            cmd = self.get_next_cmd()
        self.halted = True
        return self.op

    def has_halted(self):
        return self.halted
