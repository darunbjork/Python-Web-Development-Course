import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Practice-Task-1')))

from setup_database import Recipe, Base, engine
from sqlalchemy.orm import sessionmaker

# Setting up session
Session = sessionmaker(bind=engine)
session = Session()

def create_recipe():
    name = input("Enter the recipe name: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = input("Enter the ingredients (comma-separated): ")

    recipe = Recipe(name=name, cooking_time=cooking_time, ingredients=ingredients)
    recipe.calculate_difficulty()

    session.add(recipe)
    session.commit()
    print("Recipe added successfully!")

def view_all_recipes():
    recipes = session.query(Recipe).all()
    if recipes:
        for recipe in recipes:
            print(recipe)
            print('-' * 20)
    else:
        print("No recipes found.")

def update_recipe():
    recipe_id = int(input("Enter the ID of the recipe to update: "))
    recipe = session.get(Recipe, recipe_id)
    if recipe:
        new_name = input(f"Enter the new name (current: {recipe.name}): ")
        new_cooking_time = input(f"Enter the new cooking time (current: {recipe.cooking_time} minutes): ")
        new_ingredients = input(f"Enter the new ingredients (current: {recipe.ingredients}): ")

        if new_name:
            recipe.name = new_name
        if new_cooking_time:
            recipe.cooking_time = int(new_cooking_time)
            recipe.calculate_difficulty()
        if new_ingredients:
            recipe.ingredients = new_ingredients
            recipe.calculate_difficulty()

        session.commit()
        print("Recipe updated successfully!")
    else:
        print("Recipe not found.")

def delete_recipe():
    recipe_id = int(input("Enter the ID of the recipe to delete: "))
    recipe = session.get(Recipe, recipe_id)  
    if recipe:
        session.delete(recipe)
        session.commit()
        print("Recipe deleted successfully!")
    else:
        print("Recipe not found.")

def main():
    while True:
        print("\nRecipe Manager")
        print("1. Create a new recipe")
        print("2. View all recipes")
        print("3. Update a recipe")
        print("4. Delete a recipe")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_recipe()
        elif choice == "2":
            view_all_recipes()
        elif choice == "3":
            update_recipe()
        elif choice == "4":
            delete_recipe()
        elif choice == "5":
            session.close()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
