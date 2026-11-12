import argparse
import pandas as pd
from rich.console import Console
from rich.table import Table

parser = argparse.ArgumentParser()
parser.add_argument("csv_file")
args = parser.parse_args()

df = pd.read_csv(args.csv_file)

# Keep servers with more than 8 GB of RAM
filtered = df[df["ram_gb"] > 8]

table = Table(title="Servers with more than 8 GB RAM")

for column in filtered.columns:
    table.add_column(column)

for _, row in filtered.iterrows():
    table.add_row(*[str(value) for value in row])

console = Console()
console.print(table)

output_file = "filtered_servers.csv"
filtered.to_csv(output_file, index=False)
print(f"Saved {output_file}")