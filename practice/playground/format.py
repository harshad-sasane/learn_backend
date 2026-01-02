name = "Bob"
age = 30

# Method 1: Concatenation (annoying)
message1 = "Hello " + name + ", you are " + str(age) + " years old."

# Method 2: .format() method (better)
message2 = "Hello {}, you are {} years old.".format(name, age)

# Method 3: f-string (best!)
message3 = f"Hello {name}, you are {age} years old."
 
print(message1)
print(message2)
print(message3)
# All three produce the same string:
# "Hello Bob, you are 30 years old."
