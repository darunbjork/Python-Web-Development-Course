import pickle  # Importing the pickle module to handle binary file operations

# Function to display a recipe
def display_recipe(recipe):
    print(f"Name: {recipe['name']}")  # Print the name of the recipe
    print(f"Cooking Time: {recipe['cooking_time']} minutes")  # Print the cooking time
    print("Ingredients: " + ", ".join(recipe['ingredients']))  # Print the list of ingredients, joined by commas
    print(f"Difficulty: {recipe['difficulty']}")  # Print the difficulty level of the recipe

# Function to search for a recipe by ingredient
def search_ingredient(data):
    ingredients = data['all_ingredients']  # Get the list of all ingredients
    for index, ingredient in enumerate(ingredients):  # Enumerate over the ingredients list
        print(f"{index + 1}. {ingredient}")  # Print each ingredient with its index (starting from 1)
    try:
        choice = int(input("Enter the number of the ingredient to search for: "))  # Prompt user to select an ingredient by number
        ingredient_searched = ingredients[choice - 1]  # Get the chosen ingredient
    except (ValueError, IndexError):  # Handle invalid input or index out of range
        print("Invalid choice.")  # Print an error message for invalid choice
    else:
        recipes = data['recipes_list']  # Get the list of recipes
        for recipe in recipes:  # Loop through each recipe
            if ingredient_searched in recipe['ingredients']:  # Check if the chosen ingredient is in the recipe's ingredients
                display_recipe(recipe)  # Display the recipe if it contains the chosen ingredient

# Prompt user for the filename to load recipes from
filename = input("Enter the filename to load recipes from: ")

try:
    with open(filename, 'rb') as file:  # Open the file in read-binary mode
        data = pickle.load(file)  # Load the data from the file using pickle
except FileNotFoundError:  # Handle case where the file is not found
    print("File not found.")  # Print a file not found message
except Exception as e:  # Handle any other exceptions
    print(f"An error occurred: {e}")  # Print the error message
else:
    search_ingredient(data)  # Call the search_ingredient function if no exceptions occurred
