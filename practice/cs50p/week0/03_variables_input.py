"""
Lecture 0: Variables, Comments, Pseudocode
"""
# Ask user for their name
name = input("What's your name? ")
age = input("whats your age? ")

# Comment explaining what we're doing
# This demonstrates multiple print statements
print("hello,")
print(name)

# Using pseudocode approach
# TODO: Add age input
# TODO: Combine name and age in greeting

# Variables can change


print(f"Hello {name}, your age is {age}")

print("Hello" + str(123))
# Try breaking it
# print("Hello" + 123)  # What error do you get?
# you need to use str() to make it work otherwise it gives:  
# TypeError: can only concatenate str (not "int") to str
