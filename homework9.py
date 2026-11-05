base = float(input("Enterthe base number: "))
n = int(input("Enter the power: "))

result = 1
count = 0
while count < n:
    result *= base
    count += 1

print("Result:", result)