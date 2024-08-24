Recipe Application - Django Project

Overview

This project is a Django-based web application that allows users to create, read, update, and delete recipes. The application is built as part of a series of exercises aimed at developing and deploying a fully functional web application. Each exercise builds on the previous one, gradually introducing more features and complexity.

Exercises

Exercise 2.1: Getting Started with Django
In this exercise, we set up the development environment for the project. The main tasks included:

Creating a Virtual Environment: A virtual environment was created to isolate the project's dependencies.
Installing Django: Django was installed within the virtual environment.
Creating a New Django Project: A new Django project was initialized, and the initial structure was set up.
Running the Django Development Server: The server was started to ensure everything was set up correctly.
Files Created:

web-dev-a2: The virtual environment directory.
recipe_project: The Django project directory.
Exercise 2.2: Django Project Setup
This exercise focused on setting up the initial Django project structure and creating the necessary apps. Key tasks included:

Creating Django Apps: Three Django apps (recipes, ingredients, and users) were created to handle different parts of the application.
Linking Apps in settings.py: The apps were registered in the INSTALLED_APPS list in settings.py.
Creating Models: Models for recipes, ingredients, and users were defined.
Admin Interface Customization: The Django admin interface was customized to manage recipes and their ingredients.
Files Modified:

recipe_project/settings.py: Updated to include the new apps.
recipes/models.py, ingredients/models.py, users/models.py: Models for the respective apps were defined.
recipes/admin.py: Customized to include inline management of ingredients.
Exercise 2.3: Django Models
In this exercise, we focused on building and refining the models and database schema for the application. Key tasks included:

Creating Database Blueprints: A blueprint was created for the application's database structure, identifying the entities and their relationships.
Defining Models: Models were further refined with additional fields, constraints, and relationships.
Running Migrations: Migrations were created and applied to generate the database schema based on the defined models.
Writing Tests: Basic tests were written to ensure the models and their relationships function correctly.
Populating the Database: Sample recipes and their ingredients were added to the database via the Django admin interface.
Files Modified:

recipes/models.py, ingredients/models.py, users/models.py: Updated with additional fields and relationships.
recipes/admin.py: Further customized to enhance the admin interface.
tests.py in each app: Contains the test cases for the models.
Adding Recipes

To populate the application with sample data, three recipes were added via the Django admin interface:

Spaghetti Bolognese
A hearty Italian pasta dish with a rich meat sauce.
Chicken Caesar Salad
A classic Caesar salad with grilled chicken and homemade dressing.
Blueberry Pancakes
Fluffy pancakes loaded with fresh blueberries, perfect for breakfast.

Running the Project

To run the project locally:

Activate the Virtual Environment:
source web-dev-a2/bin/activate

Start the Development Server:
python manage.py runserver

Access the Application:
Visit http://127.0.0.1:8000/ in your web browser to access the application.
Admin interface: http://127.0.0.1:8000/admin/
Conclusion

This project showcases the step-by-step development of a Django web application, covering everything from initial setup to creating models, writing tests, and populating the database with sample data. The resulting application allows users to manage recipes and their ingredients in a user-friendly interface.
