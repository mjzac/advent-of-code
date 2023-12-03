import os
def get_input(problem_num):
    with open(f"{problem_num}.txt") as f:
        return [data.strip() for data in f.readlines()]