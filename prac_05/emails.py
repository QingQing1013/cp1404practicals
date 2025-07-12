"""
Estimate: 20
minutes
Actual: 18
minutes
"""

def main():
    """Prompt user for emails, confirm or update name, store in dictionary."""
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        default_name = get_name_from_email(email)
        response = input(f"Is your name {default_name}? (Y/n) ").strip().lower()
        if response not in ("", "y"):
            name = input("Name: ")
        else:
            name = default_name

        email_to_name[email] = name
        email = input("Email: ")

    print()

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Extract a formatted name from the given email address."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = ' '.join(parts).title()
    return name

main()