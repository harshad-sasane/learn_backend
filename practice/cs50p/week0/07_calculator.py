# Learning: input() returns strings - need float() for math!
x = float(input("enter x :"))  
y = float(input("enter y :"))

# Basic math operations
print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y}")
print(f"{x} % {y} = {x % y}")

# Testing round() function
# Syntax: round(number [, ndigits]) - [] means optional
print(f"\nround(x/y, 2): {round(x/y, 2)}")
print(f"round(x/y, 4): {round(x/y, 4)}")

# f-string formatting alternative  
print(f"f-string: {x/y:.2f}")  # .2f means 2 decimal places

# Comparing both methods
print(f"\nBoth give same result:")
print(f"round(): {round(x/y, 2)}")
print(f"f-string: {x/y:.2f}")
