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

---

# Exercise 1.5: Object-Oriented Programming in Python

## Overview

This exercise focuses on Object-Oriented Programming (OOP) concepts in Python. It covers creating custom methods, operator overloading, comparison operators, and applying these concepts to a Recipe app.

## Practice Tasks

### Practice-Task-1

- **shopping_list.py**: Script to create and manage a shopping list using custom methods in a class.
  - Add, remove, and view items in the shopping list.

### Practice-Task-2

- **height_operations.py**: Script demonstrating operator overloading.
  - Implement addition and subtraction for height objects in feet and inches.

### Practice-Task-3

- **height_comparison.py**: Script implementing comparison operators for height objects.
  - Compare height objects using <, <=, ==, >, >=, != operators.

## Main Task

### Main-Task

- **recipe_oop.py**: Object-oriented Recipe app.
  - Create Recipe class with attributes and methods.
  - Add and manage recipes.
  - Search for recipes based on ingredients.

## Virtual Environment Setup

To set up the virtual environment and install required packages, follow these steps:

1. Create a virtual environment:
   mkvirtualenv cf-python-base

Activate the virtual environment:
workon cf-python-base

Install required packages:
pip install requests==2.26.0 numpy==1.21.2

Running the Scripts

Practice-Task-1:
cd Exercise-1.5/Practice-Task-1
nano shopping_list.py
python shopping_list.py
deactivate

Practice-Task-2:
cd Exercise-1.5/Practice-Task-2
nano height_operations.py
python height_operations.py
deactivate

Practice-Task-3:
cd Exercise-1.5/Practice-Task-3
nano height_comparison.py
python height_comparison.py
deactivate

Main-Task:
cd Exercise-1.5/Main-Task
python recipe_oop.py
nano recipe_oop.py
deactivate

Requirements

All the necessary packages are listed in the requirements.txt file. To install them in a new virtual environment:

Create a new virtual environment:
mkvirtualenv cf-python-base

Activate the virtual environment:
workon cf-python-base

Install the packages:
pip install -r requirements.txt

---

### Exercise 1.6: Databases in Python

**Files:**

- **Practice-Task-1**:
  - `setup_db.py`: Script to set up the database and user for the Recipe app.
  - `requirements.txt`: Required packages for the task.
- **Practice-Task-2**:
  - `create_recipe.py`: Script to create and add recipes to the database.
  - `requirements.txt`: Required packages for the task.
- **Practice-Task-3**:
  - `search_recipe.py`: Script to search for recipes by ingredient.
  - `requirements.txt`: Required packages for the task.
- **Main-Task**:
  - `recipe_mysql.py`: Complete Recipe app using MySQL database.
  - `requirements.txt`: Required packages for the task.
  - `screenshots/`: Folder containing screenshots of the steps.
    - `step_1.png`
    - `step_2.png`
    - `step_3.png`
    - `step_4.png`

## Virtual Environment Setup

To set up the virtual environment and install required packages, follow these steps:

1. Create a virtual environment:
   mkvirtualenv cf-python-base

Activate the virtual environment:
workon cf-python-base

Install required packages:
pip install -r requirements.txt

Running the Scripts
Activate the virtual environment:
workon cf-python-base

Run the scripts:
python script_name.py

cd Exercise-1.6/Practice-Task-1
python setup_db.py
Requirements

All the necessary packages are listed in the requirements.txt file. To install them in a new virtual environment:

Create a new virtual environment:
mkvirtualenv cf-python-base

Activate the virtual environment:
workon cf-python-base

Install the packages:
pip install -r requirements.txt

---

# Exercise 1.7: Recipe Manager Application

## Overview

In this exercise, I developed a Recipe Manager application using Python, SQLAlchemy, and MySQL. The application allows users to create, view, update, and delete recipes from a MySQL database. This exercise reinforced concepts related to database integration, SQLAlchemy ORM, and handling user inputs in Python.

## Files

### Practice-Task-1:

- `setup_database.py`: Script to set up the database schema for the Recipe app using SQLAlchemy.

### Practice-Task-2:

- `create_recipe.py`: Script to create and add new recipes to the database.

### Practice-Task-3:

- `search_recipe.py`: Script to search for recipes by ingredients and perform CRUD operations.

### Main-Task:

- `recipe_manager.py`: Complete Recipe Manager application with functionalities to create, view, update, and delete recipes using SQLAlchemy and MySQL.

## Virtual Environment Setup

To set up the virtual environment and install the required packages, follow these steps:

1. Create a virtual environment:

   python3 -m venv env

Activate the virtual environment:
On macOS/Linux:
source env/bin/activate

On Windows:
.\env\Scripts\activate

Install the required packages:
pip install -r requirements.txt

Running the Scripts
Activate the virtual environment:
source env/bin/activate

Run the scripts:
python script_name.py

Example:
cd Practice-Task-1
python setup_database.py

Issues and Resolutions

Issue: ModuleNotFoundError with setup_database

Resolution: Ensured that the path to setup_database.py was correctly added to sys.path in all scripts, and the file was placed in the correct directory.

Issue: Legacy Warnings in SQLAlchemy
Resolution: Updated the SQLAlchemy code to use the Session.get() method and imported declarative_base from the recommended path.
