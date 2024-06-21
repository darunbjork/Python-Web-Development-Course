# task1.py

# Function to perform addition or subtraction
def calculate():
  """
  This function takes two numbers and an operator as input, performs the calculation, and prints the result.
  """
  a = int(input("Enter the first number: "))
  b = int(input("Enter the second number: "))
  operator = input("Enter the operator (+ or -): ")

  # Perform calculation based on the operator
  if operator == '+':
    result = a + b
  elif operator == '-':
    result = a - b
  else:
    result = "Unknown operator"

  print(f"Result: {result}")

# Call the calculate function to perform the calculation
calculate()
