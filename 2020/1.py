from itertools import combinations
from utils import get_input
from functools import reduce
import operator

input_list = list(map(int, get_input(1)))
target_sum = 2020
for n in [2, 3]:
    numbers = combinations(input_list, n)
    [
        print(reduce(operator.mul, combi, 1))
        for combi in numbers
        if sum(combi) == target_sum
    ]
