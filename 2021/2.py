import re
from utils import get_input

input_list = list(get_input(2))

x = 0
d = 0
aim = 0

def move1(direction, value):
  global x,d, aim
  if direction == "forward":
    x += value
  if direction == "down":
    d += value
  if direction == "up":
    d -= value

for command in input_list:
  match = re.search(r'(forward|down|up) (\d+)', command)
  direction = match.group(1)
  value = int(match.group(2))
  move1(direction, value)

print(x * d)

x = 0
d = 0
aim = 0

def move2(direction, value):
  global x,d, aim
  if direction == "forward":
    x += value
    d += (aim * value)
  if direction == "down":
    aim += value
  if direction == "up":
    aim -= value

for command in input_list:
  match = re.search(r'(forward|down|up) (\d+)', command)
  direction = match.group(1)
  value = int(match.group(2))
  move2(direction, value)
  
print(x * d)