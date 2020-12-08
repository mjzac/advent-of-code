from functools import reduce
import operator
from utils import get_input

the_map = [list(item) for item in get_input(3)]
col_length = len(the_map[0])
rows = len(the_map)


def traverse(curr_row, curr_col, slope):
    tree_count = 0
    right, down = slope
    while curr_row < rows:
        current_row = the_map[curr_row]
        current_col = current_row[curr_col % col_length]
        if current_col == "#":
            tree_count += 1
        curr_row += down
        curr_col += right
    return tree_count


print(traverse(1, 3, (3, 1)))
tree_list = [
    traverse(item[0], item[1], item[2])
    for item in [
        (1, 1, (1, 1)),
        (1, 3, (3, 1)),
        (1, 5, (5, 1)),
        (1, 7, (7, 1)),
        (2, 1, (1, 2)),
    ]
]

print(reduce(operator.mul, tree_list, 1))
