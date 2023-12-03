import sys
from utils import get_input


def replace_alphabets_with_empty(string):
    return [int(char)  for char in string if char.isnumeric() ]

lookup = {
  'zero': 'z0o',
  'one': 'o1e',
  'two': 't2o',
  'three': 't3e',
  'four': 'f4r',
  'five': 'f5e',
  'six': 's6x',
  'seven': 's7n',
  'eight': 'e8t',
  'nine': 'n9e'
}
def replace_words_with_number(string):
  for key, value in lookup.items():
    string = string.replace(key, value)
  return string

def solve_a(ip):
  total = 0
  for item in ip:
    modified_list = replace_alphabets_with_empty(item)
    if len(modified_list) > 0:
      total += int(f"{modified_list[0]}{modified_list[-1]}")

  return total


def solve_b(ip):
  total = 0
  for item in ip:
    modified_item = replace_words_with_number(item)
    modified_list = replace_alphabets_with_empty(modified_item)
    if len(modified_list) > 0:
      total += int(f"{modified_list[0]}{modified_list[-1]}")

  return total


def solve():
  ip = get_input(f"{sys.argv[1]}")
  if sys.argv[2] == "a":
    print(solve_a(ip))
  else:
    print("solving for b")
    print(solve_b(ip))
  
  

if __name__ == "__main__":
  solve()