from utils import get_input

input_list = list(get_input(3))


def get_digit_frequency(items):
  ip_len = len(items[0])
  zero_ctr = [0]*ip_len
  one_ctr = [0]*ip_len

  for rate in items:
    for idx, item in enumerate(rate):
      if item == '0':
        zero_ctr[idx] += 1
      if item == '1':
        one_ctr[idx] += 1
  return zero_ctr, one_ctr

zero_ctr, one_ctr = get_digit_frequency(input_list)

gamma_rate = []
epsilon_rate = []

for idx, (zero_count, one_count) in enumerate(zip(zero_ctr, one_ctr)):
  gamma_component = '0' if zero_count > one_count else '1'
  epsilon_component = '0' if zero_count < one_count else '1'
  gamma_rate.append(gamma_component)
  epsilon_rate.append(epsilon_component)


oxygen_generator_values = input_list
co2_scrubber_values = input_list

for idx in range(len(oxygen_generator_values[0])):
  zero_ctr, one_ctr = get_digit_frequency(oxygen_generator_values)
  if one_ctr[idx] >= zero_ctr[idx]:
    oxygen_generator_values = [item for item in oxygen_generator_values if item[idx] == '1']
  else:
    oxygen_generator_values = [item for item in oxygen_generator_values if item[idx] == '0']

  if len(oxygen_generator_values) == 1:
    break

for idx in range(len(co2_scrubber_values[0])):
  zero_ctr, one_ctr = get_digit_frequency(co2_scrubber_values)
  if one_ctr[idx] >= zero_ctr[idx]:
    co2_scrubber_values = [item for item in co2_scrubber_values if item[idx] == '0']
  else:
    co2_scrubber_values = [item for item in co2_scrubber_values if item[idx] == '1']
  
  if len(co2_scrubber_values) == 1:
    break


gamma_binary = "".join(gamma_rate)
epsilon_binary = "".join(epsilon_rate)

gamma_decimal = int(gamma_binary, 2)
epsilon_decimal = int(epsilon_binary, 2)

print(gamma_decimal * epsilon_decimal)

oxygen_generator_binary = oxygen_generator_values[0]
co2_scrubber_binary = co2_scrubber_values[0]

oxygen_generator_decimal = int(oxygen_generator_binary, 2)
co2_scrubber_decimal = int(co2_scrubber_binary, 2)

print(oxygen_generator_decimal * co2_scrubber_decimal)