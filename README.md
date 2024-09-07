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

---

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

---

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

---

# Recipe Application - Exercise 2.4: Django Views and Templates

## Overview

This exercise focuses on implementing the views and templates in the Recipe Application using Django. We aim to create a welcoming homepage that enhances the user interface and links to different functionalities within the application.

## Learning Goals

- Summarize the process of creating views, templates, and URLs.
- Explain how the "V" and "T" parts of MVT architecture work.
- Create a frontend page for your web application.

## Key Features

1. **Custom Welcome Page**:

   - Created a custom welcome page using Django's views and templates.
   - The homepage displays a greeting message and sets the foundation for further enhancements.

2. **Templates and Static Files**:

   - Organized the templates and static files within the app structure.
   - Implemented CSS styling to enhance the appearance of the homepage.

3. **Mapping URLs to Views**:
   - Linked the view to the corresponding URL pattern, allowing users to access the homepage by visiting the root URL.

## Instructions

1. **Setup the Project**:

   - Ensure that the virtual environment is active.
   - Navigate to the project directory.

2. **Create the View**:

   - Define the view function in the `views.py` file under the `recipes` app.
   - This view will render the `home.html` template.

3. **Create the Template**:

   - Create a `templates` folder within the `recipes` app directory.
   - Within `templates/recipes`, create the `home.html` file.
   - Add HTML and CSS content to create a welcoming design.

4. **Map the View to a URL**:

   - Create a `urls.py` file in the `recipes` app.
   - Define the URL pattern to map the view to the root URL.

5. **Run the Server**:
   - Start the Django development server and verify the changes by visiting `http://127.0.0.1:8000/`.

## File Structure

- `src/recipes/views.py`: Contains the view logic for the homepage.
- `src/recipes/urls.py`: Maps the view to the URL.
- `src/recipes/templates/recipes/home.html`: Template file for the homepage.
- `src/recipes/static/recipes/styles.css`: Stylesheet for the homepage.

## Conclusion

Exercise 2.4 is a crucial step in enhancing the user interface of the Recipe Application. By creating a custom homepage, we provide users with a more engaging and visually appealing entry point into the application. The skills learned here will be applied and expanded upon in future exercises, as we continue to develop the front end of the application.

---

# Recipe Application - Django Project

## Overview

This project is a Django-based web application that allows users to create, read, update, and delete recipes. The application is built as part of a series of exercises aimed at developing and deploying a fully functional web application. Each exercise builds on the previous one, gradually introducing more features and complexity.

## Features

- **Recipe Management**: Users can add, view, update, and delete recipes.
- **Ingredient Tracking**: Each recipe can have multiple ingredients, managed through the admin interface.
- **User Management**: Basic user authentication and profile management.

## Setup

### Prerequisites

- Python 3.x
- Virtualenv
- Django 3.x

### Installation

1. **Clone the repository**:
   git clone https://github.com/your-username/recipe-app.git

   cd recipe-app
   Create and activate a virtual environment:
   python3 -m venv web-dev-a2

source web-dev-a2/bin/activate

Install dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py migrate

Run the development server:
python manage.py runserver
Access the application at http://127.0.0.1:8000/.

Usage
Accessing the Admin Interface

Create a superuser (if you haven't already):

python manage.py createsuperuser

Access the admin interface:

Visit http://127.0.0.1:8000/admin/ and log in with the superuser credentials.

Adding Recipes
Navigate to the admin interface to add recipes and ingredients.
You can also use the frontend to create and manage recipes once the user interface is fully implemented.

Project Structure
recipe-app/
├── src/
│ ├── recipes/
│ │ ├── migrations/
│ │ ├── static/
│ │ │ └── recipes/
│ │ │ └── styles.css
│ │ ├── templates/
│ │ │ └── recipes/
│ │ │ ├── home.html
│ │ │ ├── recipe_list.html
│ │ │ └── recipe_detail.html
│ │ ├── views.py
│ │ └── urls.py
│ └── manage.py
└── web-dev-a2/

Acknowledgements:
Django Documentation - For providing comprehensive resources on Django development.
Bootstrap - Used in some templates for responsive design elements.

---

Key Exercises

Exercise 2.6: User Authentication and Navigation Bar
Implemented user authentication (login, signup, logout).
Added a dynamic navigation bar that changes based on user authentication status.
Created custom views and templates for login and signup.
Acknowledgments

Django Documentation
Bootstrap (for frontend design inspiration)
