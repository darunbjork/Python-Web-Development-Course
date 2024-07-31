# Python-Web-Development-Course

This repository contains my projects and exercises from the Python Web Development Course.

## Projects and Exercises

### Achievement-1-Python

- **Exercise-1.1**: Basic Python scripting and virtual environment setup.
  - `add.py`: A simple addition script.
  - `apple.py`: Demonstrates usage of `requests` and `numpy` packages.
  - `calculator.py`: A basic calculator script with addition, subtraction, multiplication, and division functions.

### Exercise 1.2: Data Types in Python

**Files:**

- `basic_commands.py`: Demonstrates basic commands and operations in Python.
- `variables_and_types.py`: Shows variable assignments and data types.
- `type_conversion.py`: Demonstrates explicit and implicit type conversions.
- `reassignment_increment_decrement.py`: Shows reassignment, increment, and decrement operations.
- `variable_swapping.py`: Demonstrates variable swapping.
- `expressions_arithmetic.py`: Arithmetic operations and expressions.

**Practice Task Files:**

- `Practice_Task_1/compound_interest.py`
- `Practice_Task_1/codepractice1.txt`
- `Practice_Task_2/tuples_slicing.py`
- `Practice_Task_3/lists_operations.py`
- `Practice_Task_4/strings_slicing.py`
- `Practice_Task_5/dictionaries_operations.py`
- `Practice_Task_5/recipe_app.py`

### Exercise 1.3: Operators & Functions in Python

**Files:**

- `name_capitalizer.py`: Capitalizes the user's first and last name.
- `add.py`: Adds two user-provided numbers.
- `if_else_operations.py`: Performs addition or subtraction based on user input.
- `top_scores.py`: Sorts and prints the top three test scores.
- `while_loop_numbers.py`: Prints numbers from 5 to 10.
- `recipe_app.py`: Manages recipes and calculates their difficulty.

## Virtual Environment Setup

To set up the virtual environment and install required packages, follow these steps:

1. Create a virtual environment:
   mkvirtualenv cf-python-base

Activate the virtual environment:
workon cf-python-base

Install required packages:
pip install requests numpy

Running the Scripts

Activate the virtual environment:
workon cf-python-base

Run the scripts:
To run add.py:
python add.py

To run apple.py:
python apple.py

To run calculator.py:
python calculator.py

Requirements

All the necessary packages are listed in the requirements.txt file. To install them in a new virtual environment:

Create a new virtual environment:
mkvirtualenv cf-python-base

Activate the virtual environment:
workon cf-python-base

Install the packages:
pip install -r requirements.txt

---

**Exercise 1.4**: File Handling in Python

- **Practice-Task-1**:
  - `number_list.py`: Script to write a list of numbers to a text file.
  - `number_list.txt`: Generated text file containing numbers.
- **Practice-Task-2**:
  - `recipe_binary.py`: Script to store and retrieve a recipe dictionary using pickling.
  - `recipe_binary.bin`: Generated binary file containing pickled recipes.
- **Main-Task**:
  - `recipe_input.py`: Script to take recipes from the user and store them in a binary file.
  - `recipe_search.py`: Script to search for recipes by ingredient from the binary file.

## Virtual Environment Setup

To set up the virtual environment and install required packages, follow these steps:

1. Create a virtual environment:
   ```bash
   mkvirtualenv cf-python-base
   Activate the virtual environment:
   workon cf-python-base
   ```

Install required packages:
pip install requests==2.26.0 numpy==1.21.2

Running the Scripts

Activate the virtual environment:
workon cf-python-base

Run the scripts:
To run add.py:
python add.py

To run apple.py:
python apple.py

To run calculator.py:
python calculator.py

To run number_list.py (in Practice-Task-1):

cd Exercise-1.4/Practice-Task-1
python number_list.py

To run recipe_binary.py (in Practice-Task-2):
cd Exercise-1.4/Practice-Task-2
python recipe_binary.py

To run recipe_input.py (in Main-Task):
cd Exercise-1.4/Main-Task
python recipe_input.py

To run recipe_search.py (in Main-Task):
cd Exercise-1.4/Main-Task
python recipe_search.py
Requirements

All the necessary packages are listed in the requirements.txt file. To install them in a new virtual environment:

Create a new virtual environment:
mkvirtualenv cf-python-base

Activate the virtual environment:
workon cf-python-base

Install the packages:
pip install -r requirements.txt
