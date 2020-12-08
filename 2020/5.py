from utils import get_input

boarding_passes = get_input(5)


def binary_search(input, start=0, end=127, col_start=0, col_end=7):
    row_result = -1
    col_result = -1
    for part in input:
        if part == "F":
            end = (start + end) // 2
            row_result = start
        elif part == "B":
            start = (start + end + 1) // 2
            row_result = end
        elif part == "L":
            col_end = (col_start + col_end) // 2
            col_result = col_start
        elif part == "R":
            col_start = (col_start + col_end + 1) // 2
            col_result = col_end
        else:
            pass
    return (row_result * 8) + col_result


seat_ids = [binary_search(item) for item in boarding_passes]

# part 1
print(max(seat_ids))

# part 2
sorted_seat_ids = sorted(seat_ids)
prev = sorted_seat_ids[0]
for id in sorted_seat_ids[1:]:
    if id - prev > 1:
        print(id - 1)
        break
    prev = id

