try:
    age = int(input("Enter age: "))
    if age % 2 == 0:
        print(f"{age} is even")
    else:
        print(f"{age} is odd")
except ValueError:
    print("Invalid age! Please enter numbers only")