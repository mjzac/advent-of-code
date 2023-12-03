import argparse
import subprocess
import os

parser = argparse.ArgumentParser(
    description="""Helper tool to run Advent of Code programs. 
Sample command: python aoc --day=1 --part=a """
)
parser.add_argument("--day", type=str, help="Day of the challenge")
parser.add_argument("--part", type=str, help="Part of the challenge")
args = parser.parse_args()

copy_env = os.environ.copy()
copy_env["PYTHONPATH"] = f"{os.getcwd()}"

subprocess.run(
    ["python", f"{args.day}/solution.py", f"{args.day}/{args.day}", f"{args.part}"],
    check=True,
    env=copy_env,
)
