# task3.py

# Using for loop (more concise for this specific case)
print("Using for loop:")
for i in range(10, 51, 10):
  """
  This for loop iterates from 10 to 50 (inclusive) with a step of 10,
  printing each number in the sequence.
  """
  print(i)
print("And we're done!")

# Using while loop (demonstrates loop control)
print("\nUsing while loop:")
i = 10
while i <= 50:
  """
  This while loop iterates as long as the variable 'i' is less than or equal to 50.
  Inside the loop, it prints the value of 'i' and then increments 'i' by 10.
  """
  print(i)
  i += 10
print("And we're done!")
