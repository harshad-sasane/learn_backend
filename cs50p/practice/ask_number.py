def get_valid_age():
    """Get a valid age from user with error handling."""
    while True:
        try:
            age = int(input("How old are you? "))

            if age < 0:
                print("Age cannot be less than 0! Try again.")
                continue

            if age > 120:
                print("That seems unlikely. Please enter a realistic age.")
                continue

            return age

        except ValueError:
            print("Please enter a valid number (like 25).")


# Usage is now cleaner
age = get_valid_age()
