from programming_language import ProgrammingLanguage


def main():
    # Create ProgrammingLanguage objects
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Print each language description
    print(python)
    print(ruby)
    print(visual_basic)

    # Store in a list for further processing
    languages = [python, ruby, visual_basic]

    # Filter and print dynamically typed languages
    print("\nThe dynamically typed languages are:")
    for lang in languages:
        if lang.is_dynamic():
            print(lang.name)


if __name__ == '__main__':
    main()
