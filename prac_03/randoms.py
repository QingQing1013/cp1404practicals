"""CP1404/CP5632 - Practical
Random number examples
"""
import random
# Line 1: random.randint(5, 20)
# This will print a random integer between 5 and 20, inclusive.
# Smallest possible: 5
# Largest possible: 20
print(random.randint(5, 20))
# Line 2: random.randrange(3, 10, 2)
# This will print a random odd number between 3 and 9 (not including 10), stepping by 2.
# Possible values: 3, 5, 7, 9
# Smallest possible: 3
# Largest possible: 9
# Could line 2 have produced a 4? No, because the step is 2 and the sequence starts at 3 (so it only produces odd numbers).
print(random.randrange(3, 10, 2))
# Line 3: random.uniform(2.5, 5.5)
# This will print a random float between 2.5 and 5.5, inclusive.
# Smallest possible: 2.5
# Largest possible: 5.5
print(random.uniform(2.5, 5.5))
# Code to produce a random number between 1 and 100 inclusive:
random_number = random.randint(1, 100)
print(random_number)