"""
Lecture 0: More on Strings, strip(), title()
"""
name = input("What's your name? ")

# Show the problem with whitespace
print(f"Original: '{name}'")
print(f"Length: {len(name)}")

# strip() removes whitespace
clean_name = name.strip()
print(f"After strip: '{clean_name}'")
print(f"Length now: {len(clean_name)}")

# title() capitalizes each word
titled_name = clean_name.title()
print(f"After title: '{titled_name}'")

# Chaining methods
chained_name = name.strip().title()
print(f"Chained result: '{chained_name}'")

# Other string methods
print(f"Upper: {name.upper()}")
print(f"Lower: {name.lower()}")
print(f"Swap case: {name.swapcase()}")
