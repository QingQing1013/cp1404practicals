# language_file_reader.py

from programming_language import ProgrammingLanguage

def read_languages(filename):
    """Read languages.csv and return a list of ProgrammingLanguage objects."""
    languages = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        for line in in_file:
            name, typing, refl_str, year_str, ptr_str = line.strip().split(",")

            reflection = refl_str.lower() in ("yes", "true", "1")
            pointer_arithmetic = ptr_str.lower() in ("yes", "true", "1")
            year = int(year_str)
            lang = ProgrammingLanguage(name, typing, reflection,
                                       year, pointer_arithmetic)
            languages.append(lang)
    return languages

def main():
    languages = read_languages("languages.csv")
    for lang in languages:
        print(lang)

if __name__ == "__main__":
    main()
