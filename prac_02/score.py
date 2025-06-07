"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
def main():
    score = get_valid_score()
    grade = determine_grade(score)
    print(grade)

def get_valid_score():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score

def determine_grade(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()