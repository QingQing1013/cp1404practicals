"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting.

"""
def main():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.9
    print_basic_examples(name, year, cost)
    print_guitar_summary(name, year, cost)
    print_powers_of_two()

def  print_basic_examples(name, year, cost):
    """print various examples of string formatting."""
    print("My guitar: " + name + ", first made in " + str(year))
    print("My guitar: {}, first made in {}".format(name, year))
    print("My guitar: {0}, first made in {1}".format(name, year))
    print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))

    # f-string
    print(f"My {name} was first made in {year} (that's right, {year}!)")

    # Currency formatting
    print("My {} would cost ${:,.2f}".format(name, cost))  # str.format
    print(f"My {name} would cost ${cost:,.2f}")  # f-string

    numbers = [1, 19, 123, 456, -25]
    for i, number in enumerate(numbers, 1):
      print(f"Number {i} is {number:5}")

def print_guitar_summary(name, year, cost):
    """print summary line for the guitar with formatted cost."""
    print(f"{year} {name} for about ${cost:,.0f}!")

def print_powers_of_two():
    """print powers of 2 form 2^0 to 2^10 with formatted alignment"""
    for exponent in range(11):
        result = 2 ** exponent
        print(f"2 ^ {exponent:2} is {result:4}")

main()
