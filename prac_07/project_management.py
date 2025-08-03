"""
Project Management Client Program for CP1404 Practical 07
"""
import datetime
from project import Project

DEFAULT_FILENAME = 'projects.txt'


def load_projects(filename):
    """Load projects from a tab-delimited file into a list of Project objects."""
    projects = []
    with open(filename, 'r', encoding='utf-8') as in_file:
        header = next(in_file)
        for line in in_file:
            parts = line.strip().split('\t')
            name = parts[0]
            date_str = parts[1]
            priority = int(parts[2])
            cost = float(parts[3])
            completion = int(parts[4])
            start_date = datetime.datetime.strptime(date_str, '%d/%m/%Y').date()
            projects.append(Project(name, start_date, priority, cost, completion))
    return projects


def save_projects(filename, projects):
    """Save a list of Project objects to a tab-delimited file."""
    with open(filename, 'w', encoding='utf-8') as out_file:
        out_file.write('Name\tStart Date\tPriority\tCost Estimate\tCompletion\n')
        for p in projects:
            date_str = p.start_date.strftime('%d/%m/%Y')
            out_file.write(f"{p.name}\t{date_str}\t{p.priority}\t{p.cost_estimate}\t{p.completion}\n")


def display_projects(projects):
    """Display incomplete and complete projects, sorted by priority."""
    incomplete = sorted([p for p in projects if not p.is_complete()])
    complete = sorted([p for p in projects if p.is_complete()])
    print("Incomplete projects: ")
    for p in incomplete:
        print(f"  {p}")
    print("Completed projects: ")
    for p in complete:
        print(f"  {p}")


def filter_projects_by_date(projects):
    """Prompt for a date and display projects starting after that date."""
    date_str = input('Show projects that start after date (dd/mm/YYYY): ')
    try:
        date_obj = datetime.datetime.strptime(date_str, '%d/%m/%Y').date()
    except ValueError:
        print('Invalid date format')
        return
    filtered = [p for p in projects if p.start_date > date_obj]
    filtered.sort(key=lambda p: p.start_date)
    for p in filtered:
        print(f"  {p}")


def add_project(projects):
    """Prompt user for project details and add a new Project."""
    print('Let\'s add a new project')
    name = input('Name: ')
    date_str = input('Start date (dd/mm/YYYY): ')
    start_date = datetime.datetime.strptime(date_str, '%d/%m/%Y').date()
    priority = int(input('Priority: '))
    cost = float(input('Cost estimate: '))
    completion = int(input('Percent complete: '))
    projects.append(Project(name, start_date, priority, cost, completion))


def update_project(projects):
    """List all projects sorted by name, then update selected project's completion and/or priority."""
    sorted_by_name = sorted(projects, key=lambda p: p.name)
    for i, p in enumerate(sorted_by_name):
        print(f"{i} {p}")
    choice = int(input('Project choice: '))
    project = sorted_by_name[choice]
    print(project)
    comp_str = input('New Percentage: ')
    prio_str = input('New Priority: ')
    new_comp = int(comp_str) if comp_str else None
    new_prio = int(prio_str) if prio_str else None
    project.update(new_comp, new_prio)


def print_menu():
    """Display the menu options."""
    print('- (L)oad projects')
    print('- (S)ave projects')
    print('- (D)isplay projects')
    print('- (F)ilter projects by date')
    print('- (A)dd new project')
    print('- (U)pdate project')
    print('- (Q)uit')


def main():
    print('Welcome to Pythonic Project Management')
    projects = load_projects(DEFAULT_FILENAME)
    print(f'Loaded {len(projects)} projects from {DEFAULT_FILENAME}')

    choice = ''
    while choice.lower() != 'q':
        print_menu()
        choice = input('>>> ')
        if choice.lower() == 'l':
            filename = input('Load projects from file: ')
            projects = load_projects(filename)
            print(f'Loaded {len(projects)} projects from {filename}')
        elif choice.lower() == 's':
            filename = input('Save projects to file: ')
            save_projects(filename, projects)
            print(f'Saved {len(projects)} projects to {filename}')
        elif choice.lower() == 'd':
            display_projects(projects)
        elif choice.lower() == 'f':
            filter_projects_by_date(projects)
        elif choice.lower() == 'a':
            add_project(projects)
        elif choice.lower() == 'u':
            update_project(projects)
        elif choice.lower() == 'q':
            save = input(f'Would you like to save to {DEFAULT_FILENAME}? ').lower()
            if save in ('y', 'yes'):
                save_projects(DEFAULT_FILENAME, projects)
        else:
            print('Invalid choice')

    print('Thank you for using custom-built project management software.')


if __name__ == '__main__':
    main()
