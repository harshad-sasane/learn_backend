"""
Lecture 0: Formatting Strings, f-strings
"""
name = input("What's your name? ").strip().title()

# Different ways to format strings
print("hello, " + name)  # Concatenation
print("hello,", name)    # Multiple arguments
print(f"hello, {name}")  # f-string (modern way)
print("hello, {}".format(name))  # .format() method

# f-string with expressions
print(f"Your name has {len(name)} letters")
print(f"Uppercase: {name.upper()}")
print(f"Lowercase: {name.lower()}")

# Multi-line f-string
message = f"""
Hello, {name}!

Welcome to Python programming.
Your name backwards is '{name[::-1]}'
"""
print(message)
