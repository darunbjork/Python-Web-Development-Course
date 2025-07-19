# recipe_search.py
import pickle

def display_recipe(recipe):
    print(f"\nRecipe: {recipe['name']}")
    print(f"Cooking time: {recipe['cooking_time']} minutes")
    print(f"Ingredients: {', '.join(recipe['ingredients'])}")
    print(f"Difficulty: {recipe['difficulty']}")

def search_ingredient(data):
    ingredients = data['all_ingredients']
    for idx, ingredient in enumerate(ingredients):
        print(f"{idx}: {ingredient}")

    try:
        index = int(input("Enter the number corresponding to the ingredient you want to search for: "))
        ingredient_searched = ingredients[index]
    except (ValueError, IndexError):
        print("Invalid input.")
        return

    print(f"\nRecipes containing {ingredient_searched}:")
    for recipe in data['recipes_list']:
        if ingredient_searched in recipe['ingredients']:
            display_recipe(recipe)

filename = input("Enter the filename to search recipes: ")

try:
    with open(filename, 'rb') as file:
        data = pickle.load(file)
    search_ingredient(data)
except FileNotFoundError:
    print("File not found.")
except:
    print("An error occurred.")

