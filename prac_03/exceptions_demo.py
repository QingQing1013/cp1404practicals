"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    - A ValueError occurs when the user inputs something that cannot be converted to an integer,
      such as letters or symbols (e.g., "abc", "3.14", "!").

2. When will a ZeroDivisionError occur?
    - A ZeroDivisionError occurs when the user enters 0 for the denominator,
      which makes the division undefined.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    - Yes. You can check if the denominator is zero before performing the division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(f"Result: {fraction}")
except ValueError:
    print("Numerator and denominator must be valid integers!")

print("Finished.")