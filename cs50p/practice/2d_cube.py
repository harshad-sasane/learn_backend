# Paste this into Python Tutor
print("Making a 3x3 square:")
print("-------------------")

for row in range(3):           # Outer loop for rows
    print(f"\nRow {row} starting...")
    
    for col in range(3):       # Inner loop for columns
        print(f"  Column {col}: Printing #")
        # print("#", end="")  # Uncomment this to see actual square
    
    print(f"Row {row} finished.")
    
print("\nSquare complete!")