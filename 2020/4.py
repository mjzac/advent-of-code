import re
from utils import get_input

passports = get_input(4)

required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
current_entries = []
valid_passport_count = 0


def validate_byr(value):
    sanatised_val = int(value.strip())
    return (
        True
        if sanatised_val is not None and sanatised_val >= 1920 and sanatised_val <= 2002
        else False
    )


def validate_iyr(value):
    sanatised_val = int(value.strip())
    return (
        True
        if sanatised_val is not None and sanatised_val >= 2010 and sanatised_val <= 2020
        else False
    )


def validate_eyr(value):
    sanatised_val = int(value.strip())
    return (
        True
        if sanatised_val is not None and sanatised_val >= 2020 and sanatised_val <= 2030
        else False
    )


def validate_hgt(value):
    if "cm" in value:
        value = value.replace("cm", "")
        sanatised_val = int(value)
        return (
            True
            if sanatised_val is not None
            and sanatised_val >= 150
            and sanatised_val <= 193
            else False
        )
    elif "in" in value:
        value = value.replace("in", "")
        sanatised_val = int(value)
        return (
            True
            if sanatised_val is not None and sanatised_val >= 59 and sanatised_val <= 76
            else False
        )
    else:
        return False


def validate_hcl(value):
    num_pattern = "#[0-9a-f]{6}$"
    num_result = re.match(num_pattern, value)
    return num_result


def validate_ecl(value):
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def validate_pid(value):
    num_pattern = "[0-9]{9}$"
    num_result = re.match(num_pattern, value)
    return num_result


validators = {
    "byr": validate_byr,
    "iyr": validate_iyr,
    "eyr": validate_eyr,
    "hgt": validate_hgt,
    "hcl": validate_hcl,
    "ecl": validate_ecl,
    "pid": validate_pid,
}

for entry in passports:
    if entry == "":
        is_valid = len(
            [True for key in required_keys if key in current_entries]
        ) == len(required_keys)
        if is_valid:
            valid_passport_count += 1
        # reset the validation
        current_entries = []
    else:
        for item in entry.split(" "):
            [key, value] = item.split(":")
            validator = validators.get(key)
            # part 1
            # current_entries += [key]

            # Part2
            if validator:
                if validator(value.strip()):
                    current_entries += [key]
print(valid_passport_count)
