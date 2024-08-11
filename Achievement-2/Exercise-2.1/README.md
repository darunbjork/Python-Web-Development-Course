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
