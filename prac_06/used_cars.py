"""CP1404/CP5632 Practical - Client code to use the Car class."""
from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(f"Fuel after refueling: {limo.fuel}")

    limo.drive(115)
    print(limo)

main()
