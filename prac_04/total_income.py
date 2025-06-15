"""
CP1404/CP5632 Practical
Refactored cumulative total income program
"""

def main():
    """Display income report for incomes over a given number of months."""
    number_of_months = int(input("How many months? "))
    incomes = get_incomes(number_of_months)
    print_income_report(incomes)


def get_incomes(number_of_months):
    """Prompt user for income values and return a list of incomes."""
    incomes = []
    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    return incomes


def print_income_report(incomes):
    """Print income report showing each month's income and cumulative total."""
    print("\nIncome Report\n-------------")
    total = 0
    for month_index, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {month_index:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()
