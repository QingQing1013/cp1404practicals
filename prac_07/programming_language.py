# programming_language.py

class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        """Initialise a ProgrammingLanguage with all five attributes."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __str__(self):
        return (f"{self.name} ({self.year}) – Typing: {self.typing}, "
                f"Reflective: {self.reflection}, "
                f"Pointer Arithmetic: {self.pointer_arithmetic}")
