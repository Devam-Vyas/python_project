rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, i + 1):  # Inner loop for columns
        print(j, end=" ")   # Print star
    print()

rows = int(input("Enter the row size for the pattern: "))
for i in range(rows, 0, -1):  # Outer loop for rows in reverse
    for j in range(1, i + 1):  # Inner loop for columns
        print(j, end=" ")   # Print star
    print()

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(rows  - i):  # Inner loop for spaces
        print(" ", end=" ")
    for k in range(1, 2 * i):  # Inner loop for stars
        print("*", end=" ")
    print()

rows = int(input("Enter the row size for the pattern: "))
for i in range(rows , 0, -1):  # Outer loop for rows in reverse
    for j in range(rows  - i):  # Inner loop for spaces
        print(" ", end=" ")
    for k in range(1, 2 * i):  # Inner loop for stars
        print("*", end=" ")
    print()  # Move to the next line

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, i + 1):  # Inner loop for columns
        if j == 1 or i == rows or i == j:  # Print star on borders
            print("*", end=" ")
        else:
            print(" ", end=" ")  # Print space inside
    print()
