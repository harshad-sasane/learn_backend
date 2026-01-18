# get_int_function.py
def get_int(prompt):
    """Repeatedly prompt the user until they enter a valid integer."""
    while True:
        try:
            return int(input(prompt))  # Success! Return immediately.
        except ValueError:
            print("That's not a valid integer.")

def main():
    # Now our main program is clean and simple
    x = get_int("What's x? ")
    y = get_int("What's y? ")
    print(f"The sum of {x} + {y} = {x + y}")

if __name__ == "__main__":
    main()