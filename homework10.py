num = int(input("Enter a number: "))

count = 0

if num == 0:
    count = 1
else:

    num = abs(num)
    while num > 0:
        num = num // 10
        count = count + 1

print("Total digits =", count)