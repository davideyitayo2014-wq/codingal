# Square it Out! - Getting Started with Lists

# Get range from user
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

# Create list of square values
square_list = []
for num in range(start, end + 1):
    square_list.append(num ** 2)

# Separate odd and even values
odd_values = []
even_values = []

for val in square_list:
    if val % 2 == 0:
        even_values.append(val)
    else:
        odd_values.append(val)

# Display results
print(f"\nSquare values between {start} and {end}: {square_list}")
print(f"Even squares: {even_values}")
print(f"Odd squares: {odd_values}")