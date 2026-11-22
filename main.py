print("=== PYTHON CALCULATOR 3.0 ===")

while True:
    try:
        number1 = float(input("First number: "))
        operator = input("Operator (+, -, *, /, **): ")
        number2 = float(input("Second number: "))

        if operator == "+":
            result = number1 + number2

        elif operator == "-":
            result = number1 - number2

        elif operator == "*":
            result = number1 * number2 

        elif operator == "/":
            if number2 == 0:
                print("Error Division by zero!")
                continue
            result = number1 / number2

        elif operator =="**":
            result = number1 ** number2

        else:
            print("Invalid Operator!")
            continue

        print(f"Result: {result:g}")

    except ValueError:
        print("Error: Enter valid numbers!")

    again = input("Continue? (y/n): ")

    if again.lower() != "y":
        print("Goodbye!")
        break
        

