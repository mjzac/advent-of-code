from collections import defaultdict
from utils import get_input

input_list = list(map(int, list(get_input(6))[0].split(',')))

timers = defaultdict(int)
for timer in input_list:
  timers[timer] += 1

def get_count(timers, days=80):
  for _ in range(days):
    new_timers = defaultdict(int)
    for day,count in timers.items():
      days_left = day - 1
      if days_left < 0:
        days_left = 6
        new_timers[8] += count
      new_timers[days_left] += count
    timers = new_timers
  return sum(timers.values())

print(get_count(timers))
print(get_count(timers, days=256))