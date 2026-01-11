"""
Lecture 0: def, Returning Values
"""
# Basic function
def hello():
    print("hello, world")

hello()

# Function with parameter
def greet(name):
    print(f"hello, {name}")

greet("Harshad")
greet(name="David")

# Function with return value
def square(x):
    return x * x

result = square(5)
print(f"5 squared is {result}")

# Multiple return values
def get_name():
    first = "John"
    last = "Doe"
    return first, last

first_name, last_name = get_name()
print(f"{first_name} {last_name}")

# Default parameters
def greet_with_time(name, time_of_day="day"):
    return f"Good {time_of_day}, {name}!"

print(greet_with_time("Alice"))
print(greet_with_time("Bob", "morning"))
