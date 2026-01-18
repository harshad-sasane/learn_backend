while True:
    try:
        # 1. Get input
        fraction = input("Fraction: ")

        # 2. Parse structure (split)
        parts = fraction.split("/")
        if len(parts) != 2:
            print("Invalid format. Use X/Y format.")
            continue

        # 3. Convert types
        x = int(parts[0])
        y = int(parts[1])

        # 4. Validate logic (not exceptions)
        if x > y:
            print("Numerator cannot be larger than denominator.")
            continue
        if x < 0 or y < 0:
            print("No negative numbers allowed.")
            continue

        # 5. Compute value
        percentage = (x / y) * 100
        rounded = round(percentage)

        # 6. Format output
        if rounded <= 1:
            print("E")
        elif rounded >= 99:
            print("F")
        else:
            print(f"{rounded}%")

        # Success! Exit loop
        break

    except ValueError:
        print("Invalid input. Use integers in X/Y format.")
    except ZeroDivisionError:
        print("Denominator cannot be zero.")
