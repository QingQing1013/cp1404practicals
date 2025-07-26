import random
from car import Car


class UnreliableCar(Car):
    """A Car that might not drive depending on its reliability percentage."""

    def __int__(self, name, feel, reliability):
        """Initialise an UnreliableCar with a reliability percentage."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive, but only succeed if a random chance allows it."""
        chance = random.uniform(0, 100)
        if chance < self.reliability:
            return super().drive(distance)
        else:
            return 0
