from guitar import Guitar
from datetime import date

CURRENT_YEAR = date.today().year

def test_guitar(guitar, expected_age, expected_vintage):
    age = guitar.get_age()
    vintage = guitar.is_vintage()
    print(f"{guitar.name} get_age() - Expected {expected_age}. Got {age}")
    print(f"{guitar.name} is_vintage() - Expected {expected_vintage}. Got {vintage}")


def main():
    # Create test guitars
    g1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    g2 = Guitar("Another Guitar", 2013, 2000.00)

    # Expected results based on current year
    test_guitar(g1, CURRENT_YEAR - 1922, True)
    test_guitar(g2, CURRENT_YEAR - 2013, False)

if __name__ == "__main__":
    main()