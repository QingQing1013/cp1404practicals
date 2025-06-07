"""
CP1404/CP5632 - Practical
Menu

"""
def main():
    MENU = ("(G)et a score  (P)rint result  (S)how stars  (Q)uit")
    print(MENU)
    choice = input("> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_score_result(score)
            print(f"Result: {result}")
        elif choice == "S":
            print("*" * int(score))
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("> ").upper()


def get_valid_score():
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score

def determine_score_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"





main()