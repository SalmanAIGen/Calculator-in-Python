# Calculator-in-Python

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /, **, %): ")

if operator == "+":
    result = a + b
    print(f"The result of {a} + {b} is: {result}")
elif operator == "-":
    result = a - b
    print(f"The result of {a} - {b} is: {result}")
elif operator == "*":
    result = a * b
    print(f"The result of {a} * {b} is: {result}")
elif operator == "/":
    result = a / b
    print(f"The result of {a} / {b} is: {result}")
elif operator == "**":
    result = a ** b
    print(f"The result of {a} ** {b} is: {result}")
elif operator == "%":
    result = a % b
    print(f"The result of {a} % {b} is: {result}")
else:
    print("Invalid operator")