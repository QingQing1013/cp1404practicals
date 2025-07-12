"""
Project class definition for CP1404 Project Management Program
"""
import datetime

class Project:
    """Represent a project with its details."""
    def __init__(self, name, start_date, priority, cost_estimate, completion=0):
        """
        Initialise a Project.

        start_date: datetime.date object or string in 'dd/mm/YYYY' format
        priority: int (1 = highest)
        cost_estimate: float
        completion: int (0-100)
        """
        # If start_date is string, parse to date
        if isinstance(start_date, str):
            self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        else:
            self.start_date = start_date
        self.name = name
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    def __str__(self):
        """Return a formatted string for this project."""
        date_str = self.start_date.strftime("%d/%m/%Y")
        return (f"{self.name}, start: {date_str}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion}%")

    def __lt__(self, other):
        """Sort projects by priority (lower number = higher priority)."""
        return self.priority < other.priority

    def is_complete(self):
        """Return True if project is 100% complete."""
        return self.completion >= 100

    def update(self, new_completion=None, new_priority=None):
        """Update completion percentage and/or priority."""
        if new_completion is not None:
            self.completion = new_completion
        if new_priority is not None:
            self.priority = new_priority


