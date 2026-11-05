# Tuple Product

# Given tuple - you can change the values
my_tuple = (2, 4, 6, 8, 10)

# Method 1: Using loop (best for beginners)
product = 1
for num in my_tuple:
    product = product * num

print(f"Given tuple: {my_tuple}")
print(f"Product of all numbers: {product}")

# Method 2: Using math.prod (Python 3.8+) - shorter version
import math
print(f"\nProduct using math.prod: {math.prod(my_tuple)}")