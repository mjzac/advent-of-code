from itertools import permutations

from intcode import Intcode


def reset_program():
    with open("7input.txt") as f:
        program = list(map(int, f.readline().split(",")))
    return program


def calculate_max_output(settings, feedback_mode=False):
    thrust_signals = {}
    program = reset_program()
    for setting in settings:
        op = 0
        amplifiers = [Intcode(program, ip_seq=[]) for i in range(5)]
        initialized_phase_setting = False
        while not amplifiers[-1].has_halted():
            for idx, amplifier in enumerate(amplifiers):
                if not initialized_phase_setting:
                    amplifier.add_ip(setting[idx])
                amplifier.add_ip(op)
                op = amplifier.execute(feedback_mode=feedback_mode)
            initialized_phase_setting = True
        thrust_signals[setting] = op
    return sorted(thrust_signals.items(), key=lambda x: x[1], reverse=True)[0][1]


def part1():
    settings = list(permutations(range(5)))
    print(calculate_max_output(settings))


def part2():
    settings = list(permutations(range(5, 10)))
    print(calculate_max_output(settings, feedback_mode=True))


if __name__ == "__main__":
    part1()
