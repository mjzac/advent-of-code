from copy import deepcopy
from itertools import zip_longest
from utils import get_input

input_list = list(get_input(4))
input_list = [item for item in input_list if len(item) > 0]
numbers_drawn = input_list[0].split(',')
input_list = input_list[1:]

class Board:
  def __init__(self, entries) -> None:
      self.mapping = {}
      for row_idx,row in enumerate(entries):
        cleaned_row = row.replace('  ', ' ')
        numbers = cleaned_row.split(' ')
        for col_idx,number in enumerate(numbers):
          self.mapping[number] = (row_idx, col_idx)

      self.winning_combinations = []
      self.last_drawn_number = None
      for r_idx in range(len(entries)):
        self.winning_combinations.append([(r_idx, c) for c in range(len(entries))])
        self.winning_combinations.append([(c, r_idx) for c in range(len(entries))])


  def mark(self, number):
    has_won = []
    try:
      row_idx, col_idx = self.mapping[number]
      t_copy = deepcopy(self.winning_combinations)
      for idx, combination in enumerate(self.winning_combinations):
        for cm_idx, (r_idx, c_idx) in enumerate(combination):
          if r_idx == row_idx and c_idx == col_idx:
            del t_copy[idx][cm_idx]
            has_won.append(len(t_copy[idx]) == 0)
            
            
      self.winning_combinations = t_copy
      self.last_drawn_number = int(number)
      del self.mapping[number]
    except KeyError:
      pass
    return any(has_won)

  def get_score(self):
    return self.last_drawn_number * sum(map(int,self.mapping.keys()))


def grouper(iterable, n, fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


game_boards = []
for a in grouper(input_list, 5):
  game_boards.append(Board(list(a)))


winning_boards = []
for drawn_number in numbers_drawn:
  for board in game_boards:
    result = board.mark(drawn_number)
    if result:
      winning_boards.append(board)
  game_boards = [board for board in game_boards if board not in winning_boards]

print(f"First board: {winning_boards[0].get_score()}")
print(f"Last board: {winning_boards[-1].get_score()}")