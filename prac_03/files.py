def main():
    write_name_to_file()
    read_name_from_file()
    add_first_two_numbers()
    sum_all_numbers()

def write_name_to_file():
    name = input("Enter your name: ")
    file = open('name.txt', 'w')
    file.write(name)
    file.close()
    return name

def read_name_from_file():
    file = open('name.txt', 'r')
    name = file.read().strip()
    file.close()
    print(f"Hi {name}!")

def add_first_two_numbers():
    with open('numbers.txt', 'r') as file:
        first = int(file.readline())
        second = int(file.readline())
    print(first + second)

def sum_all_numbers():
    total = 0
    with open('numbers.txt', 'r') as file:
        for line in file:
            total += int(line)
    print(total)

main()