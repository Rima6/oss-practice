import argparse
from tabulate import tabulate

parser = argparse.ArgumentParser()
parser.add_argument("--name", required=True)
args = parser.parse_args()

students = [
    ["Python", "Programming"],
    ["Tabulate", "Table formatting"],
    ["GitHub", "Code sharing"]
]

print(f"Hello, {args.name}!")
print(tabulate(students, headers=["Tool", "Purpose"], tablefmt="grid"))
