num1_str = input("Enter the first number: ")
num1 = float(num1_str)

num2_str = input("Enter the second number: ")
num2 = float(num2_str)

operation = input("Enter the operation (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operation. Please use +, -, *, or /.")
