from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A special taxi with higher fare based on fanciness and flagfall."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi with Fanciness multiplier."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return fare with flagfall, rounded as per parent class."""
        fare = super().get_fare() + self.flagfall
        return fare

    def __str__(self):
        """Return string representation, including flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
