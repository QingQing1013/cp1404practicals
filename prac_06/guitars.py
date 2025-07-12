from guitar import Guitar


def main():
    print("My guitars!")
    guitars = []
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        vintage_str = " (vintage)" if guitar.is_vintage() else ""
        print(f"{guitar.name} ({guitar.year}) : ${guitar.cost:,.2f}{vintage_str} added.\n")

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_str = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_str}")

if __name__ == "__main__":
    main()