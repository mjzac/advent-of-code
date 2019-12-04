# https://adventofcode.com/2019/day/4


def check(num_str, part="a"):
    is_monotonic = True
    has_double = False
    prev_digit = "-1"
    occurences = 1
    has_exact_pair = False
    for digit in num_str:
        if digit < prev_digit:
            is_monotonic = False
            break
        if digit == prev_digit:
            has_double = True
            occurences += 1
        else:
            if occurences == 2:
                has_exact_pair = True
            occurences = 1
        prev_digit = digit
    if occurences == 2:
        has_exact_pair = True
    return is_monotonic and (has_double if part is "a" else has_exact_pair)


def run_a():
    ip = list(map(int, "256310-732736".split("-")))
    valid_password_count = 0
    for num in range(ip[0], ip[1] + 1):
        num_str = str(num)
        if check(num_str, "a"):
            valid_password_count += 1

    return valid_password_count


def run_b():
    ip = list(map(int, "256310-732736".split("-")))
    valid_password_count = 0
    for num in range(ip[0], ip[1] + 1):
        num_str = str(num)
        if check(num_str, "b"):
            valid_password_count += 1

    return valid_password_count


def tests():
    assert check("111111", part="a") is True
    assert check("223450", part="a") is False
    assert check("123789", part="a") is False

    assert check("112233", part="b") is True
    assert check("123444", part="b") is False
    assert check("111122", part="b") is True


if __name__ == "__main__":
    tests()
    print(run_b())
