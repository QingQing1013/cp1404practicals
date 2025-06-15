# Part 1: Collect 5 numbers from the user and report statistics

numbers = []

# Ask the user for 5 numbers
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

# Output the required details
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")

# Part 2: Woefully inadequate security checker

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye','swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username_input = input("Username: ")

if username_input in usernames:
    print("Access granted")
else:
    print("Access denied")
