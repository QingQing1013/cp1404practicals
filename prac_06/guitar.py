from datetime import date

class Guitar:
    """Represent a guitar with name, year, and cost."""
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the guitar's age in years."""
        current_year = date.today().year
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is at least 50 years old."""
        return self.get_age() >= 50