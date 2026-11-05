try:
    num1, num2 = eval(input("Enter two numbers, seperated by a comma : "))
    result = num1 / num2
    print("Rsult is", result)


except ZeroDivisionError:
    print("Division by zero is error !!")

except SyntaxError:
    print("comma is missing. Enter numbers separated by comma like this 1, 2")

except:
    print("Wrong input")

else:
    print("No exceptions")

finally:
    ("This will execute no matter what")