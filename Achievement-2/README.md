# Achievement-2: Django Web Development

## Overview

This achievement focuses on getting started with Django, a high-level Python web framework that encourages rapid development and clean, pragmatic design. The exercises in this achievement cover setting up a Django environment, understanding the basics of Django projects and apps, and getting familiar with Django's built-in tools and functionality.

## Exercise 2.1: Setting Up Django

### Files

- **Django_Getting_Started_Answers.txt:** Documentation and answers for the initial Django setup and configuration.

### Steps

1. **Environment Setup:**
   - Verified Python version: Python 3.8.19.
   - Created a virtual environment named `achievement2` using `mkvirtualenv`.
   - Activated and deactivated the virtual environment using `workon` and `deactivate`.
2. **Installing Django:**
   - Installed Django version 4.2.15 and its dependencies using `pip install django`.
   - Verified the Django installation using `django-admin --version`.

### How to Run

1. **Activate the Virtual Environment:**
   workon achievement2
   Start Django Development Server:
   (Steps to be updated as the project progresses.)

Deactivating the Virtual Environment:
deactivate

Virtual Environment Setup

To set up the virtual environment and install required packages, follow these steps:

Create a virtual environment:
mkvirtualenv achievement2

Activate the virtual environment:
workon achievement2

Install Django:
pip install django

Check Django version:
django-admin --version

---

## Overview

This achievement focuses on developing a web application using the Django framework. In this exercise, we set up the structure for a Django project and explored the difference between Django projects and apps. The exercise also involved running the Django development server, creating a superuser, and understanding the project’s basic structure.

## Exercise 2.2: Django Project Set Up

### Files

- **proj_contents_before_renaming.jpg**: Screenshot of the project structure before renaming the project directory.
- **proj_contents_after_renaming.jpg**: Screenshot of the project structure after renaming the project directory.
- **django_server_success.jpg**: Screenshot of the Django server running successfully on localhost.
- **admin-dashboard.jpg**: Screenshot of the Django admin dashboard showing the superuser.

### Steps

#### Project Structure Setup:

- **Created Project Directory**: Created a folder named `A2_Recipe_App`.
- **Virtual Environment**: Created and activated a virtual environment named `a2-ve-recipeapp`.
- **Installed Django**: Installed Django 4.2.15 in the virtual environment.
- **Created Django Project**: Initialized the Django project named `recipe_project`.
- **Renamed Project Directory**: Renamed the `recipe_project` directory to `src`.
- **Ran Migrations**: Applied migrations to set up the initial database schema.

#### Django Development Server:

- **Run Server**: Started the Django development server and confirmed it was running on `http://127.0.0.1:8000/`.

#### Superuser Creation:

- **Created Superuser**: Created a superuser for accessing the Django admin interface.

### How to Run

#### Start the Django Development Server:

1. **Activate the Virtual Environment**:

   workon a2-ve-recipeapp

2. **Navigate to the `src` Directory**:

   cd ~/path/to/your/A2_Recipe_App/src

3. **Run Migrations**:

   python manage.py migrate

4. **Start the Server**:

   python manage.py runserver

#### Deactivating the Virtual Environment:

deactivate

Virtual Environment Setup
To set up the virtual environment and install required packages, follow these steps:

Create a virtual environment:
mkvirtualenv a2-ve-recipeapp

Activate the virtual environment:
workon a2-ve-recipeapp

Install Django:
pip install django

Check Django version:
django-admin --version

---

Exercise 2.3: Creating and Managing Django Apps

Files
recipe_app_screenshot.png: Screenshot of the Django admin interface showing the Recipe, Ingredient, and Category models.
Steps
App Creation:

Recipes App:
Created the recipes app to manage recipe data.
Defined the Recipe model with fields for the recipe's name, description, and related ingredients and categories.
Ingredients App:
Created the ingredients app to manage individual ingredients.
Defined the Ingredient model with fields for the ingredient's name and quantity.
Categories App:
Created the categories app to categorize recipes.
Defined the Category model with a name field.
Setting Up Relationships:

Established a ManyToManyField relationship between Recipe and Ingredient in the recipes app to allow a recipe to include multiple ingredients.
Linked Recipe to Category using a ForeignKey in the recipes app to categorize recipes.
Admin Interface:

Registered the Recipe, Ingredient, and Category models in the Django admin site.
Customized the admin interface to display and manage the models effectively.
Migrations and Testing:

Ran makemigrations and migrate to apply the database schema changes.
Created a superuser and used the admin interface to add sample data for recipes, ingredients, and categories.
Verified the correct setup by running the Django tests and interacting with the admin panel.

How to Run

Activate the Virtual Environment:
workon a2-ve-recipeapp

Navigate to the src Directory:
cd ~/path/to/your/A2_Recipe_App/src

Run Migrations:
python manage.py makemigrations
python manage.py migrate

Create a Superuser:
python manage.py createsuperuser

Start the Server:
python manage.py runserver
Access the Django Admin Interface:
Navigate to http://127.0.0.1:8000/admin/ and log in with the superuser credentials.

Add Sample Data:
Use the admin interface to add categories, ingredients, and recipes.

Deactivating the Virtual Environment:
deactivate

Virtual Environment Setup
To set up the virtual environment and install required packages, follow these steps:

Create a virtual environment:
mkvirtualenv a2-ve-recipeapp

Activate the virtual environment:
workon a2-ve-recipeapp

Install Django:
pip install django

Check Django version:
django-admin --version

---

## Exercise 2.4: Django Views and Templates

### Overview

This exercise focused on creating views and templates in Django to render HTML content dynamically. The primary objective was to set up a custom homepage for the recipe application by defining a view, creating a corresponding template, and mapping a URL to the view.

### Files

- `views.py`: Contains the `home` view responsible for rendering the homepage.
- `recipes_home.html`: The template file that defines the structure of the homepage.
- `urls.py`: Maps the root URL to the `home` view.

### Steps

#### 1. View Creation:

- Defined the `home` view in the `recipes` app to render the homepage.

#### 2. Template Creation:

- Created the `recipes_home.html` file under `recipes/templates/recipes/` to hold the HTML content for the homepage.

#### 3. URL Mapping:

- Configured `urls.py` in the `recipes` app to map the root URL to the `home` view.
- Updated the main project’s `urls.py` to include the `recipes` app’s URLs.

#### 4. Running the Server:

- Started the Django development server and accessed the homepage at `http://127.0.0.1:8000/`.

### How to Run

#### 1. Start the Django Development Server:

- Activate the Virtual Environment: `workon a2-ve-recipeapp`
- Navigate to the `src` Directory: `cd ~/path/to/your/A2_Recipe_App/src`
- Run the Server: `python manage.py runserver`

#### 2. Access the Homepage:

- Open your web browser and navigate to `http://127.0.0.1:8000/`.

#### 3. Deactivating the Virtual Environment:

- `deactivate`

### Future Improvements

- Implement additional views and templates for other parts of the application.
- Enhance the homepage with more advanced HTML and CSS, and consider adding dynamic content from the database.
