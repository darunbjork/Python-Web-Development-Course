# if_else_operations.py
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter an operator (+ or -): ")

if operator == "+":
    print(f"The result is: {num1 + num2}")
elif operator == "-":
    print(f"The result is: {num1 - num2}")
else:
    print("Unknown operator")

