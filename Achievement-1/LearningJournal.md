# Learning Journal

## Setting Up the Environment

Today, I set up my development environment for the Python Web Development Course. This included installing Python 3.8.19 and Homebrew. I also created a new virtual environment named `alpha` and installed the `requests` and `numpy` packages.

## Creating and Running Python Scripts

I created three Python scripts:

1. `add.py`: A simple script that adds two numbers.
2. `apple.py`: Demonstrates usage of the `requests` and `numpy` packages.
3. `calculator.py`: A basic calculator script with functions for addition, subtraction, multiplication, and division.

I also learned how to activate and deactivate virtual environments and how to run Python scripts within these environments.

## Documenting and Preparing for Deployment

I created the `README.md` and `LearningJournal.md` files to document my progress and prepare for deploying the project on GitHub. I also ensured that all necessary packages are listed in the `requirements.txt` file and can be easily installed in a new virtual environment.

## Challenges and Solutions

- **Issue**: Encountered problems with importing `requests` and `numpy` in `apple.py` in VS Code.
  - **Solution**: Fixed the issue by opening a new terminal in VS Code and activating the virtual environment before running `pip install requests numpy`.

---

## Exercise 1.2: Data Types in Python

### Observations

- Learned how to work with different data types in Python.
- Understood the differences between scalar and non-scalar data types.
- Explored various operations and methods for tuples, lists, strings, and dictionaries.

### Challenges

- Faced issues with understanding the nuances of dictionary operations, but resolved them through practice.
- Had to carefully manage data types to avoid type errors.

### What I've Learned

- Basics of data types and variables in Python.
- Creating and manipulating tuples, lists, strings, and dictionaries.
- Applying data structures to a practical task, such as a recipe app.

### Detailed Steps

1. **Basic Commands and Operations**:
   - Created `basic_commands.py` to demonstrate basic commands and operations in Python.
2. **Variable Assignments and Data Types**:
   - Created `variables_and_types.py` to show variable assignments and data types.
3. **Type Conversions**:
   - Created `type_conversion.py` to demonstrate explicit and implicit type conversions.
4. **Reassignment, Increment, and Decrement Operations**:
   - Created `reassignment_increment_decrement.py` to show reassignment, increment, and decrement operations.
5. **Variable Swapping**:
   - Created `variable_swapping.py` to demonstrate variable swapping.
6. **Arithmetic Operations and Expressions**:
   - Created `expressions_arithmetic.py` to perform arithmetic operations and expressions.

### Practice Tasks

1. **Practice Task 1**:

   - Created `compound_interest.py` to calculate compound interest.
   - Created `codepractice1.txt` to store input values for the compound interest calculation.

2. **Practice Task 2**:

   - Created `tuples_slicing.py` to practice tuples and slicing operations.

3. **Practice Task 3**:

   - Created `lists_operations.py` to perform various list operations.

4. **Practice Task 4**:

   - Created `strings_slicing.py` to practice string slicing operations.

5. **Practice Task 5**:
   - Created `dictionaries_operations.py` to perform dictionary operations.
   - Created `recipe_app.py` to manage recipes using dictionaries.

### Documentation and Deployment

- Documented my progress in the `README.md` and `LearningJournal.md` files.
- Ensured that all necessary packages are listed in the `requirements.txt` file and can be easily installed in a new virtual environment.

### Challenges and Solutions

- **Issue**: Encountered a "FileNotFoundError" while running the compound interest script.
  - **Solution**: Ensured the `codepractice1.txt` file was created and in the correct directory before running the script.
- **Issue**: Had difficulty with tuples and slicing operations initially.
  - **Solution**: Reviewed Python documentation and examples to better understand these concepts.

---

## Exercise 1.3: Operators & Functions in Python

### Observations

- Learned how to implement conditional statements in Python to determine program flow.
- Used loops to reduce time and effort in Python programming.
- Wrote functions to organize Python code.

### Challenges

- Faced issues with understanding nested loops, but resolved them through practice.
- Had to carefully manage variable scopes to avoid conflicts.

### What I've Learned

- How to use if-else statements, for loops, and while loops in Python.
- How to define and call functions with and without arguments.
- How to use list comprehensions for concise code.

### Detailed Steps

1. **Creating `name_capitalizer.py`**:
   - Created a script to capitalize the user's first and last name.
2. **Creating `add.py`**:
   - Created a script to add two user-provided numbers.
3. **If-Else Statements**:
   - Created `if_else_operations.py` to perform addition or subtraction based on user input.
4. **For Loops**:
   - Created `top_scores.py` to sort and print the top three test scores.
5. **While Loops**:
   - Created `while_loop_numbers.py` to print numbers from 5 to 10.
6. **Functions**:
   - Created `recipe_app.py` to manage recipes and calculate their difficulty.

### Practice Tasks

1. **Practice Task 1**:
   - Used if-else statements to perform operations based on user input.
2. **Practice Task 2**:
   - Used for loops to sort and print the top three scores.
3. **Practice Task 3**:
   - Used while loops to print numbers in a range.

### Documentation and Deployment

- Documented my progress in the `README.md` and `LearningJournal.md` files.
- Ensured that all necessary packages are listed in the `requirements.txt` file and can be easily installed in a new virtual environment.

### Challenges and Solutions

- **Issue**: Faced issues with variable scope in nested functions.
  - **Solution**: Reviewed Python documentation on scopes and implemented global variables as needed.

---

# Learning Journal

## Exercise 1.4: File Handling in Python

### Observations

- Learned how to work with files in Python for reading and writing data.
- Understood the difference between text files and binary files.
- Explored pickling to store complex data structures.
- Practiced error handling using try-except blocks.

### Challenges

- Encountered issues with handling file paths and navigating directories.
- Faced difficulties in understanding the nuances of binary file handling and pickling.

### What I've Learned

- Basics of file handling in Python, including reading and writing to text files.
- How to use the `pickle` module to work with binary files.
- Techniques for handling errors and exceptions to make scripts more robust.
- Navigating directories and handling file operations using the `os` module.

### Detailed Steps

1. **File Reading and Writing**:
   - Created `number_list.py` to write a list of numbers to a text file.
2. **Binary File Handling**:
   - Created `recipe_binary.py` to store and retrieve a recipe dictionary using pickling.
3. **Managing Recipes**:
   - Created `recipe_input.py` to take recipes from the user and store them in a binary file.
   - Created `recipe_search.py` to search for recipes by ingredient from the binary file.
4. **Error Handling**:
   - Implemented error handling in file operations to manage file not found errors and other exceptions.

### Practice Tasks

1. **Practice Task 1**:
   - Created `number_list.py` to practice writing a list of numbers to a text file.
2. **Practice Task 2**:
   - Created `recipe_binary.py` to practice binary file handling using the `pickle` module.

### Documentation and Deployment

- Documented progress in the `README.md` and `LearningJournal.md` files.
- Ensured that all necessary packages are listed in the `requirements.txt` file and can be easily installed in a new virtual environment.

### Challenges and Solutions

- **Issue**: Encountered a "FileNotFoundError" while accessing a file.
  - **Solution**: Implemented try-except blocks to handle the error and provide user-friendly prompts.
- **Issue**: Had difficulty understanding pickling.
  - **Solution**: Reviewed Python documentation and examples to better understand pickling and binary file handling.

---

## Exercise 1.5: Object-Oriented Programming in Python

### Observations

- Learned the basics of Object-Oriented Programming (OOP) in Python.
- Understood how to create and use classes and objects.
- Explored the concepts of inheritance, polymorphism, and operator overloading.
- Practiced writing custom methods and handling class variables.

### Challenges

- Initially struggled with understanding inheritance and polymorphism.
- Faced difficulties in implementing comparison operators and operator overloading.

### What I've Learned

- How to create classes and define data and procedural attributes.
- Implementing getter and setter methods.
- Using inheritance to create a hierarchy of classes.
- Operator overloading and defining custom operators.
- Polymorphism and using methods with the same name in different classes.

### Detailed Steps

1. **Custom Methods**:
   - Created `shopping_list.py` to manage a shopping list using custom methods in a class.
2. **Operator Overloading**:
   - Created `height_operations.py` to demonstrate addition and subtraction of height objects.
3. **Comparison Operators**:
   - Created `height_comparison.py` to implement and test comparison operators for height objects.
4. **Recipe App**:
   - Created `recipe_oop.py` to build a Recipe app using OOP concepts.
   - Defined a Recipe class with methods to add ingredients, calculate difficulty, and search for recipes.

### Practice Tasks

1. **Practice Task 1**:
   - Created `shopping_list.py` to practice custom methods in a class.
2. **Practice Task 2**:
   - Created `height_operations.py` to practice operator overloading.
3. **Practice Task 3**:
   - Created `height_comparison.py` to practice comparison operators.

### Documentation and Deployment

- Documented progress in the `README.md` and `LearningJournal.md` files.
- Ensured all necessary packages are listed in the `requirements.txt` file and can be easily installed in a new virtual environment.

### Challenges and Solutions

- **Issue**: Struggled with understanding inheritance.
  - **Solution**: Reviewed examples and practiced by creating a hierarchy of classes.
- **Issue**: Difficulty in implementing comparison operators.
  - **Solution**: Practiced by defining and testing each comparison operator.

---

## Exercise 1.6: Databases in Python

### Observations

- Learned how to set up and connect to a MySQL database using Python.
- Explored basic SQL commands to create databases, users, and tables.
- Practiced error handling when working with databases.

### Challenges

- Encountered issues with MySQL server not starting and managing permissions.
- Faced difficulties in integrating SQL commands with Python scripts.

### What I've Learned

- Setting up and starting MySQL server.
- Creating databases and users in MySQL.
- Writing Python scripts to interact with MySQL database.
- Implementing CRUD (Create, Read, Update, Delete) operations using SQL.

### Detailed Steps

1. **Setting up MySQL Server**:
   - Started MySQL server and created a database and user.
   - Implemented error handling for server start issues.
2. **Practice Task 1**:
   - Created `setup_db.py` to set up the database and user.
3. **Practice Task 2**:
   - Created `create_recipe.py` to add recipes to the database.
4. **Practice Task 3**:
   - Created `search_recipe.py` to search for recipes by ingredient.
5. **Main Task**:
   - Created `recipe_mysql.py` to implement a full CRUD Recipe app using MySQL.

### Practice Tasks

1. **Practice Task 1**:
   - Created `setup_db.py` to practice setting up a database and user.
2. **Practice Task 2**:
   - Created `create_recipe.py` to practice adding recipes to the database.
3. **Practice Task 3**:
   - Created `search_recipe.py` to practice searching for recipes by ingredient.

### Documentation and Deployment

- Documented progress in the `README.md` and `LearningJournal.md` files.
- Ensured all necessary packages are listed in the `requirements.txt` file and can be easily installed in a new virtual environment.

### Challenges and Solutions

- **Issue**: MySQL server not starting.
  - **Solution**: Fixed permissions and ensured the correct path for MySQL server.
- **Issue**: Difficulty in integrating SQL commands with Python scripts.
  - **Solution**: Reviewed Python documentation on `mysql-connector` and practiced SQL commands.
