# Basic while loop
count = 0
while count < 3:
    print(f"Count is: {count}")
    count += 1  # IMPORTANT: Don't forget this!

# Output:
# Count is: 0
# Count is: 1
# Count is: 2

# Backend example: Retry logic
attempts = 0
max_attempts = 3
connection_successful = False

while attempts < max_attempts and not connection_successful:
    print(f"Connection attempt {attempts + 1}")
    # Try to connect to database here
    # If successful: connection_successful = True
    attempts += 1
