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
