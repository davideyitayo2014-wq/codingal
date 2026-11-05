# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Method 1: Using symmetric_difference()
result1 = set1.symmetric_difference(set2)
print("Using symmetric_difference():", result1)

# Method 2: Using the ^ operator
result2 = set1 ^ set2
print("Using ^ operator:", result2)

# Example with arrays (lists)
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Convert lists to sets before computing
result3 = set(list1).symmetric_difference(set(list2))
print("From lists:", result3)
