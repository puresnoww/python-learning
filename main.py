print(""=== PYTHON CALCULATOR ==="")

num1 = float(input("Enter first number: "))
operator = input("Choose operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Results:", num1 + num2)
elif operator == "-":
    print("Results:", num1 - num2)
elif operator == "*":
    print("Results:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: division by zero!")
else:
    print("Unknown operator!")
    