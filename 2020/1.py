from utils import get_input

input_list = list(map(int, get_input(1)))
target_sum = 2020

for num in input_list:
    needed_num = abs(target_sum - num)
    if needed_num in input_list:
        print("Result {}".format(needed_num * num))
        break

