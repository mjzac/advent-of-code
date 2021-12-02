from utils import get_input

input_list = list(map(int, get_input(1)))

depth_increasing = -1
previous_depth = -1
for depth in input_list:
  if depth > previous_depth:
    depth_increasing += 1
  previous_depth = depth

print(depth_increasing)

depth_increasing = -1
prev_window_sum = -1
for d1,d2,d3 in zip(input_list, input_list[1:], input_list[2:]):
  window_sum = d1 + d2 +d3
  if window_sum > prev_window_sum:
    depth_increasing += 1
  prev_window_sum = window_sum
print(depth_increasing)
