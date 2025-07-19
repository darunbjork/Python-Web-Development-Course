# recipe_binary.py
import pickle

# Creating a recipe dictionary
recipe = {
    'name': 'Tea',
    'ingredients': ['Tea leaves', 'Water', 'Sugar'],
    'cooking_time': 5,
    'difficulty': 'Easy'
}

# Writing the recipe to a binary file
with open('recipe_binary.bin', 'wb') as file:
    pickle.dump(recipe, file)

# Reading the recipe from the binary file
with open('recipe_binary.bin', 'rb') as file:
    loaded_recipe = pickle.load(file)

# Displaying the loaded recipe
print(f"Recipe: {loaded_recipe['name']}")
print(f"Ingredients: {', '.join(loaded_recipe['ingredients'])}")
print(f"Cooking time: {loaded_recipe['cooking_time']} minutes")
print(f"Difficulty: {loaded_recipe['difficulty']}")

