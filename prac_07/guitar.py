# guitar.py

class Guitar:
    """Represent a guitar with name, year, and cost."""
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        """Allow sorting Guitars by year (oldest to newest)."""
        return self.year < other.year
