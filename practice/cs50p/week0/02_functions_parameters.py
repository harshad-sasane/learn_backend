"""
Lecture 0: Functions, Bugs, Parameters
"""
# The print function with different arguments
print("hello", "world", "!")
print("hello", "world", "!", sep="-")
print("hello", "world", end="!!!\n")
print("no new line here", end="")

# Parameters experiment
print("\n--- Testing end parameter ---")
print("Line 1", end=" | ")
print("Line 2", end=" | ")
print("Line 3")

# Breaking it on purpose - see the error
# print("hello" "world")  # Uncomment to see error
