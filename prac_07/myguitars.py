# myguitars.py

from guitar import Guitar

def load_guitars(filename):
    """Read guitars.csv and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r', encoding='utf-8') as in_file:
        for line in in_file:
            name, year_str, cost_str = line.strip().split(',')
            guitars.append(Guitar(name, int(year_str), float(cost_str)))
    return guitars

def save_guitars(filename, guitars):
    """Write all guitars out to the CSV file."""
    with open(filename, 'w', encoding='utf-8') as out_file:
        for g in guitars:
            out_file.write(f"{g.name},{g.year},{g.cost}\n")

def display_guitars(title, guitars):
    """Print a heading and each guitar on its own line."""
    print(title)
    for g in guitars:
        print(f"  {g}")
    print()

def main():
    filename = 'guitars.csv'
    guitars = load_guitars(filename)

    display_guitars("Your guitars:", guitars)

    guitars.sort()
    display_guitars("Guitars sorted by year (oldest→newest):", guitars)

    # Let the user add a new guitar
    print("Add a new guitar:")
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitars.append(Guitar(name, year, cost))

    # Save back to file
    save_guitars(filename, guitars)
    print(f"\nUpdated {filename} with your new guitar.")

if __name__ == '__main__':
    main()
