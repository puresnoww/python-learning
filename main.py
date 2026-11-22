print("=== PYTHON CALCULATOR 2.0 ===")

while True:
    num1 = float(input("\nFirst number: "))
    operator = input("Operator (+, -, *, /): ")
    num2 = float(input("Second number: "))

    if operator == "+":
        print("Result:", num1 + num2)
    elif operator == "-":
        print("Result:", num1 - num2)
    elif operator == "*":
        print("Result:", num1 * num2)
    elif operator == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero!")
    else:
        print("Unknown operator!")

    again = input("\nContinue? (y/n): ")

    if again.lower() != "y":
        print("Goodbye!")
        break
