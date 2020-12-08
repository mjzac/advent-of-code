from utils import get_input

input_list = get_input(2)
policy_password = [
    (item.split(": ")[0].split(" "), item.split(": ")[1]) for item in input_list
]


part1_valid_count = 0
part2_valid_count = 0
for policy, password in policy_password:
    criteria = policy[1]
    min_occurance = int(policy[0].split("-")[0])
    max_occurance = int(policy[0].split("-")[1])
    if (
        password.count(criteria) >= min_occurance
        and password.count(criteria) <= max_occurance
    ):
        part1_valid_count += 1
    position = int(policy[0].split("-")[0]) - 1
    next_position = int(policy[0].split("-")[1]) - 1
    if criteria == password[position] or criteria == password[next_position]:
        if criteria == password[position] and criteria == password[next_position]:
            pass
        else:
            part2_valid_count += 1

print(part1_valid_count, part2_valid_count)
