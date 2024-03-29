VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors():
    """In the while loop ask the user to enter a color,
       lowercase it and store it in a variable. Next check:
       - if 'quit' was entered for color, print 'bye' and break.
       - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
       - otherwise print the color in lower case."""
    while True:
        user_input = str(input("Kindly Enter a color of your choice: ")).lower().strip()

        if user_input == "quit":
            print("bye")
            break
        elif user_input in VALID_COLORS:
            print(user_input)
        else:
            print("Not a valid color")
            continue

print_colors()