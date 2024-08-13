n = 4  # Take input N

# Print the top half of the pyramid including the middle
for i in range(1, n + 1):
    leading_spaces = "  " * (n - i)  # Two spaces for each level of indentation
    if i == 1:
        print(leading_spaces + str(i))  # Print the first row with only one number
    else:
        middle_spaces = " " * (2 * i - 3)  # Calculate the middle spaces using progression rule
        print(leading_spaces + str(i) + middle_spaces + str(i))  # Print numbers on both sides with middle spaces

# Print the bottom half of the pyramid
for i in range(n - 1, 0, -1):
    leading_spaces = "  " * (n - i)  # Maintain symmetry with top half
    if i == 1:
        print(leading_spaces + str(i))  # Print last row with only one number
    else:
        middle_spaces = " " * (2 * i - 3) 
        right_number = n + n-i+1 
        print(leading_spaces + str(i) + middle_spaces + str(right_number))