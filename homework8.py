age = int(input("Enter your age: "))

if age >= 13:
    if age <= 20:
       print("your age is between 13 to 20 years. you are a teenager.")
    else:
        print("your age is above 20 years. Not in the 13-20 range.")
else:
    print("Your age is below 13 years. not in the 13-20 range.")
