# https://adventofcode.com/2019/day/3/
the_grid = [x[:] for x in [[None] * 20000] * 20000]  # ~3GB memory usage :/
origin = (6000, 5000)
intersections = []

print("Grid ready")


def parse_cmd_to_idx(cmd, curr_x, curr_y):
    """
    Parses the command and return `(next_x, next_y, num_steps, negative_direction)`
    """
    direction = cmd[0]
    steps = int(cmd[1:])
    if direction is "U":
        return (curr_x, curr_y - steps, steps, True)
    elif direction is "D":
        return (curr_x, curr_y + steps, steps, False)
    elif direction is "R":
        return (curr_x + steps, curr_y, steps, False)
    elif direction is "L":
        return (curr_x - steps, curr_y, steps, True)
    raise ValueError


def part1(x, y):
    intersections.append((abs(x - origin[0]) + abs(y - origin[1])))


def part2(x, y, steps):
    intersections.append(the_grid[x][y][1] + steps)


def set_point_visited(x, y, wire_number, steps):
    try:
        current_value = the_grid[x][y]
        if current_value is not None and current_value[0] != wire_number:
            part2(x, y, steps)
            # part1(x, y)
            the_grid[x][y] = "X"
        else:
            the_grid[x][y] = (wire_number, steps)
    except IndexError:
        print(x, y)
        exit(1)


def traverse(cmd, curr_x, curr_y, wire_num, steps_taken):
    next_x, next_y, steps, negative_direction = parse_cmd_to_idx(cmd, curr_x, curr_y)
    if next_x == curr_x:
        # traverse along y axis
        range_start_idx = (
            max(curr_y, next_y) if negative_direction else min(curr_y, next_y)
        )
        range_end_idx = (
            min(curr_y, next_y) if negative_direction else max(curr_y, next_y)
        )
        range_step = -1 if negative_direction else 1
        for idx, y_cord in enumerate(range(range_start_idx, range_end_idx, range_step)):
            set_point_visited(curr_x, y_cord, wire_num, steps_taken + idx)

    if next_y == curr_y:
        # traverse along x axis
        range_start_idx = (
            max(curr_x, next_x) if negative_direction else min(curr_x, next_x)
        )
        range_end_idx = (
            min(curr_x, next_x) if negative_direction else max(curr_x, next_x)
        )
        range_step = -1 if negative_direction else 1
        for idx, x_cord in enumerate(range(range_start_idx, range_end_idx, range_step)):
            set_point_visited(x_cord, curr_y, wire_num, steps_taken + idx)

    return (next_x, next_y, steps_taken + steps)


def run():
    with open("3input.txt") as f:
        wire_one_path = f.readline().split(",")
        curr_x = origin[0]
        curr_y = origin[1]
        steps_taken = 0
        for cmd in wire_one_path:
            curr_x, curr_y, steps_taken = traverse(cmd, curr_x, curr_y, 1, steps_taken)

        curr_x = origin[0]
        curr_y = origin[1]
        wire_two_path = f.readline().split(",")
        steps_taken = 0
        for cmd in wire_two_path:
            curr_x, curr_y, steps_taken = traverse(cmd, curr_x, curr_y, 2, steps_taken)

        return sorted(intersections)[1]


if __name__ == "__main__":
    print(run())
