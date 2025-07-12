class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """
        Initialise a ProgrammingLanguage instance.
        name: str, the name of the language
        typing: str, either "Static" or "Dynamic"
        reflection: bool, whether the language supports reflection
        year: int, first appearance year
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language uses dynamic typing."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return a descriptive string for the ProgrammingLanguage."""
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, "
                f"First appeared in {self.year}")

