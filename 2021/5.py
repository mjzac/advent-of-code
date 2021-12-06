from collections import defaultdict
from utils import get_input, Vector2D

input_list = list(get_input(5))


class Vent:
  def __init__(self, start: Vector2D, end: Vector2D) -> None:
      self._start = start
      self._end = end

  @property
  def start(self):
    return self._start

  @property
  def end(self):
    return self._end

vents: list[Vent] = []

for line in input_list:
  coordinates = line.split(' -> ')
  p1 = list(map(int, coordinates[0].split(',')))
  p2 = list(map(int, coordinates[1].split(',')))

  start = Vector2D(p1[0], p1[1])
  end = Vector2D(p2[0], p2[1])

  vents.append(Vent(start, end))



def get_overlaps(vents: list[Vent]):
  mapping = defaultdict(int)
  for v in vents:
    heading = v.start.unit_vector(v.end)
    pt = v.start
    while pt != v.end:
      mapping[pt] += 1
      pt += heading
      
    # Include end point
    mapping[pt] += 1
  return len([value for value in mapping.values() if value > 1])

part1_vents = [v for v in vents if v.start.x == v.end.x or v.start.y == v.end.y]

print(get_overlaps(part1_vents))
print(get_overlaps(vents))
