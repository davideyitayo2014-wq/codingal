# Check the frequency of a value in dictionary

# Sample test dictionary
test_dict = {'a': 10, 'b': 20, 'c': 10, 'd': 20, 'e': 30, 'f': 10}

# Value to check frequency for
value_to_check = 10

# Count frequency
frequency = 0
for v in test_dict.values():
    if v == value_to_check:
        frequency += 1

print(f"Dictionary: {test_dict}")
print(f"Frequency of {value_to_check} is: {frequency}")

# --- If you want to count frequency of ALL values ---

freq_dict = {}
for val in test_dict.values():
    if val in freq_dict:
        freq_dict[val] += 1
    else:
        freq_dict[val] = 1

print(f"\nFrequency of all values: {freq_dict}")