Learning Journal

Exercise 2.1: Getting Started with Django

Goals:

To set up a Python virtual environment and install Django.
To create a basic Django project and ensure the development server runs correctly.

Activities
Created a virtual environment using venv to isolate the project dependencies.
Installed Django within the virtual environment using pip.
Initialized a new Django project called recipe_project.
Verified the setup by running the Django development server and accessing the default Django welcome page.

Challenges
Understanding the structure of a Django project was a bit challenging at first, but the documentation and the exercise materials were helpful in explaining it.
Setting up the virtual environment required some troubleshooting, but it was resolved by ensuring the correct Python version was used.

Outcomes
Successfully set up the Django environment and created the initial project structure.
The Django development server ran without any issues, confirming that the setup was correct.

Reflections
This exercise was a great introduction to Django. Setting up the environment properly is crucial, as it forms the foundation for the entire project.
Running the development server and seeing the Django welcome page was a satisfying first step in this project.

Exercise 2.2: Django Project Setup

Goals:
To create and structure the Django project by adding apps and defining models.
To customize the Django admin interface for managing the application's data.

Activities
Created three Django apps: recipes, ingredients, and users.
Defined models for each app, representing the main entities of the application: recipes, ingredients, and users.
Registered the apps in the INSTALLED_APPS list in settings.py.
Customized the Django admin interface to manage recipes and their associated ingredients more efficiently by using inline models.

Challenges
Defining the relationships between models (e.g., linking ingredients to recipes) required careful planning and understanding of Django's ORM.
Customizing the admin interface to include inline models was a new concept but very useful for managing related objects.
Outcomes
Successfully created and linked the apps, and the models were defined and registered.
The Django admin interface was enhanced, allowing for efficient data management of recipes and ingredients.

Reflections
The process of setting up apps and defining models is essential in shaping how the data is structured and managed in the application.
Customizing the admin interface was a valuable skill to learn, as it greatly improves the usability of the backend.
Exercise 2.3: Django Models

Goals:

To refine the database models and create a schema that represents the application's data structure.
To write tests for the models to ensure they work as intended.
To populate the application with sample data.

Activities
Created a database blueprint to outline the relationships between entities (e.g., recipes, ingredients, categories).
Refined the models by adding necessary fields and relationships (e.g., difficulty, category).
Ran migrations to update the database schema according to the defined models.
Wrote basic tests to validate the models and ensure data integrity.
Added sample recipes to the application via the Django admin interface.

Challenges
Adding non-nullable fields to existing models required providing default values during the migration process, which required careful consideration of what defaults would be appropriate.
Writing tests for models was straightforward but required attention to detail to ensure all edge cases were covered.

Outcomes
The database schema was successfully defined and implemented through migrations.
The models were tested, and the tests passed successfully, confirming that the models work as intended.
The application was populated with sample data, making it more functional and ready for further development.

Reflections
This exercise highlighted the importance of planning and testing when working with models and databases in Django.
Writing tests early in the development process is crucial for catching potential issues before they become bigger problems.
