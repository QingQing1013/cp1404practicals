from unreliable_car import UnreliableCar
def main():
    reliable_car = UnreliableCar("Reliable", 100, 100)
    unreliable_car = UnreliableCar("Unreliable", 100, 30)

    always_driven = 0
    for _ in range(10):
        driven = reliable_car.drive(10)
        always_driven += driven
    print(f"ReliableCar driven {always_driven}km (should be 100)")

    driven_total = 0
    for _ in range(100):
        driven_total += unreliable_car.drive(1)
    print(f"UnreliableCar drove {driven_total} km out 100 attempts (expected ~30)")

if __name__ == "__main__":
    main()
