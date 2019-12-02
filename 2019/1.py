# https://adventofcode.com/2019/day/1


def get_fuel(mass):
    return mass // 3 - 2


def get_fuel_with_additional_fuel(mass, total_fuel=0):
    if mass <= 0:
        return total_fuel
    fuel = max(get_fuel(mass), 0)
    return get_fuel_with_additional_fuel(fuel, total_fuel + fuel)


with open("1input.txt") as f:
    fuel_required = 0
    for line in f:
        module_mass = int(line)
        fuel_required += get_fuel_with_additional_fuel(module_mass)
    print(fuel_required)
