def get_input(problem_num):
    with open("inputs/{}.txt".format(problem_num)) as f:
        return [data.strip() for data in f.readlines()]
