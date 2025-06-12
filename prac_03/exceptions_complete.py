"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # ✅ TODO: this line – we exit the loop after valid input
    except ValueError:  # ✅ TODO - specify the exception we want to catch
        print("Please enter a valid integer.")

print("Valid result is:", result)
