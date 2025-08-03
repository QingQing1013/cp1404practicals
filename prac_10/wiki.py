"""
CP1404/CP5632 Practical
Wikipedia API: Get page details from user input with exception handling
"""

import wikipedia
import warnings

# Suppress BeautifulSoup parser warning
warnings.filterwarnings("ignore", category=UserWarning, module="wikipedia")

def main():
    print("Wikipedia Search")
    while True:
        title = input("Enter page title: ").strip()
        if not title:
            print("Thank you.")
            break
        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)
        except wikipedia.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')

if __name__ == "__main__":
    main()
