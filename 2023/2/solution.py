import sys

from utils import get_input

max_counts = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def game_is_possible(draw_results):
    for color, max_count in max_counts.items():
        if draw_results[color] > max_count:
            return False
    return True


def extract_game_data(row):
    game_parts, draws_data = row.split(":")
    game_parts = game_parts.replace("Game ", "")
    game_id = int(game_parts)
    draws_data = draws_data.split(";")
    sanatized_draws_data = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for each_draw in draws_data:
        draw_results = each_draw.strip().split(",")
        for each_result in draw_results:
            count, color = each_result.strip().split(" ")
            sanatized_draws_data[color] = max(sanatized_draws_data[color], int(count))
    return (game_id, sanatized_draws_data)


def solve_a(ip):
    total = 0
    for row in ip:
        game_id, sanatized_draws_data = extract_game_data(row)
        if game_is_possible(sanatized_draws_data):
            total += game_id

    return total


def solve_b(ip):
    total = 0
    for row in ip:
        game_id, sanatized_draws_data = extract_game_data(row)
        set_power = (
            sanatized_draws_data["red"]
            * sanatized_draws_data["green"]
            * sanatized_draws_data["blue"]
        )
        total += set_power

    return total


def solve():
    ip = get_input(f"{sys.argv[1]}")
    if sys.argv[2] == "a":
        print(solve_a(ip))
    else:
        print(solve_b(ip))


if __name__ == "__main__":
    solve()
