# Learning Journal: Achievement-2

## Exercise 2.1: Setting Up Django

### Observations

- Successfully set up the Django environment and installed Django version 4.2.15.
- Explored the creation and management of virtual environments using `virtualenvwrapper`.

### Challenges

- **Challenge:** Understanding the environment setup process.
  - **Solution:** Reviewed the `virtualenvwrapper` documentation and practiced activating/deactivating the environment multiple times.

### What I've Learned

- **Django Installation:** Learned how to install Django and verify its installation.
- **Virtual Environment Management:** Gained proficiency in creating, activating, and deactivating virtual environments using `virtualenvwrapper`.
- **Python Environment Management:** Familiarized with Python version management and virtual environment setup.

### Detailed Steps

1. **Python Version Check:**

   - Verified that Python 3.8.19 is installed and working correctly.

2. **Virtual Environment Setup:**

   - Created a new virtual environment named `achievement2` using `mkvirtualenv`.
   - Activated and deactivated the environment using `workon` and `deactivate`.

3. **Django Installation:**
   - Installed Django using `pip` and confirmed the installation using `django-admin --version`.

---

### `Achievement-2/Exercise-2.2/LearningJournal.md`

# Learning Journal: Achievement-2

## Exercise 2.2: Django Project Set Up

### Observations

- Successfully set up the Django project structure and renamed the project directory.
- Ran the Django development server and verified the successful setup on localhost.
- Created and managed a Django superuser for accessing the admin interface.

### Challenges

- **Challenge**: Understanding the differences between Django projects and apps.
  - **Solution**: Reviewed Django documentation and explored the project and app structures by creating the `recipe_project`.
- **Challenge**: Renaming the project directory while maintaining the correct project structure.
  - **Solution**: Carefully followed the steps to rename the project directory and confirmed that the project still functioned correctly.

### What I've Learned

- **Django Project Structure**: Gained an understanding of the basic components of a Django project and how apps fit into this structure.
- **Project and App Differences**: Learned the distinction between a Django project and an app, and how apps can be reused across multiple projects.
- **Running the Django Server**: Learned how to start the Django development server and access the application on localhost.
- **Superuser Creation**: Acquired the skills to create a superuser and log in to the Django admin panel.

### Detailed Steps

#### Project Structure Setup:

- **Project Directory Creation**:
  - Created a new directory named `A2_Recipe_App`.
  - Initialized the Django project within this directory.
- **Virtual Environment**:

  - Created and activated a virtual environment named `a2-ve-recipeapp`.
  - Installed Django and set up the project structure.

- **Directory Renaming**:
  - Renamed the `recipe_project` directory to `src` to clarify the project structure.
- **Migration and Server Setup**:
  - Applied initial migrations to set up the database schema.
  - Started the Django development server and accessed it through `http://127.0.0.1:8000/`.

#### Superuser Creation:

- Created a superuser for the Django project and logged in to the admin interface.

---

Exercise 2.3: Creating and Managing Django Apps

Observations
Successfully created three Django apps: recipes, ingredients, and categories.
Set up models for each app and established relationships between them.
Integrated the apps with the Django admin interface to manage data through the admin panel.
Performed database migrations and verified the correct setup by running tests and interacting with the admin interface.
Challenges
Challenge: Understanding the relationships between different models in Django.
Solution: Referred to the Django documentation on model relationships and experimented with different field types like ForeignKey and ManyToManyField.
Challenge: Ensuring that the migrations correctly reflected the model changes.
Solution: Ran makemigrations and migrate commands frequently to incrementally build the database schema and resolve any issues.
What I've Learned
App Creation and Management: Learned how to create multiple Django apps within a project and manage their settings.
Model Design: Gained experience in designing Django models and establishing relationships between them using fields like ForeignKey and ManyToManyField.
Admin Interface Customization: Learned how to register models with the Django admin and customize their display.
Migrations and Database Management: Developed skills in using Django's migration system to manage database schema changes.
Detailed Steps
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
Future Improvements
Views and Templates: Plan to create views and templates to display recipes, ingredients, and categories on the website.
User Interaction: Explore creating forms to allow users to submit recipes directly through the website.
API Development: Consider exposing the data through a RESTful API using Django REST Framework for potential mobile app integration.
