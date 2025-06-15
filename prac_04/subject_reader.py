"""
CP1404/CP5632 Practical
Data file -> lists program
"""
FILENAME = "subject_data.txt"

def main():
    data = load_data()
    display_subject_details(data)

def load_data():
    """Read data from file and return a list of [subject, lecturer, number of students]."""
    subject_list = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            if len(parts) != 3:
                print(f"Warning: Skipping malformed line: {line}")
                continue
            try:
                parts[2] = int(parts[2])
                subject_list.append(parts)
            except ValueError:
                print(f"Warring: Invalid number on line: {line}")
    return subject_list

def display_subject_details(subjects):
    """Display subject data in readable format."""
    for subject_code, lecturer, student_count in subjects:
        print(f"{subject_code} is taught by {lecturer} and has {student_count:3} students.")

main()
