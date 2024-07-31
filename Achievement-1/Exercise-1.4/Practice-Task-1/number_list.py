# number_list.py
numbers = [str(num) + '\n' for num in range(50, 101)]
with open('number_list.txt', 'w') as file:
    file.writelines(numbers)

