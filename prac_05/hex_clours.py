"""
CP1404 practical
hex colour lookup
"""
Colour_to_hex = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "Aqua": "#00ffff", "Aquamarine": "#7fffd4",
                 "Azure": "#f0ffff", "Beige": "#f5f5dc", "Bisque": "#ffe4c4", "Black": "#000000",
                 "BlanchedAlmond": "#ffebcd", "Blue": "#0000ff"}
colour_name = input("Enter colour name: ").title()
while colour_name != "":
    try:
        print(f"{colour_name}: {Colour_to_hex[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ")
