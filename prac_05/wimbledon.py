"""
Wimbledon Champions
Estimate: 30 minutes
Actual:   ? minutes
"""

FILENAME = "wimbledon.csv"


def main():
    records = read_wimbledon_data(FILENAME)
    champion_to_wins = count_champions(records)
    countries = extract_countries(records)

    print("Wimbledon Champions:")
    for name, wins in champion_to_wins.items():
        print(f"{name} {wins}")

    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def read_wimbledon_data(filename):
    """Read the wimbledon.csv file and return a list of [year, country, champion]."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        records = [line.strip().split(",") for line in in_file]
    return records


def count_champions(records):
    """Return a dictionary of champion names and how many times they won."""
    champion_to_wins = {}
    for record in records:
        champion = record[2]
        if champion in champion_to_wins:
            champion_to_wins[champion] += 1
        else:
            champion_to_wins[champion] = 1
    return champion_to_wins


def extract_countries(records):
    """Return a set of unique countries from the data."""
    countries = {record[1] for record in records}
    return countries


main()
