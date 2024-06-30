# Step 1: Open a file called “number_list.txt” in write mode
with open('number_list.txt', 'w') as file:
    # Step 2: Create a list of numbers from 50 to 100
    numbers = [str(i) + '\n' for i in range(50, 101)]
    # Step 3: Write the list to the file using writelines()
    file.writelines(numbers)
