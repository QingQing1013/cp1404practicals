from silver_service_taxi import SilverServiceTaxi

def main():
    taxi = SilverServiceTaxi("Fancy Taxi", 100, 2)
    taxi.drive(18)  # 18 km
    fare = taxi.get_fare()
    print(f"Fare for 18km: ${fare:.2f}")
    assert fare == 48.8, f"Expected $48.80, got {fare}"

    print(taxi)

if __name__ == "__main__":
    main()
