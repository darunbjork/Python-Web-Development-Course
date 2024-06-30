import pickle

# Step 2: Make a quick recipe for tea
recipe = {
    'name': 'Tea',
    'ingredients': ['Tea leaves', 'Water', 'Sugar'],
    'cooking_time': 5,
    'difficulty': 'Easy'
}

# Step 3: Store the dictionary in a binary file
with open('recipe_binary.bin', 'wb') as file:
    pickle.dump(recipe, file)

# Step 4: Load your data back and display the recipe
with open('recipe_binary.bin', 'rb') as file:
    loaded_recipe = pickle.load(file)

print("Recipe details:")
print(f"Name: {loaded_recipe['name']}")
print(f"Ingredients: {', '.join(loaded_recipe['ingredients'])}")
print(f"Cooking Time: {loaded_recipe['cooking_time']} minutes")
print(f"Difficulty: {loaded_recipe['difficulty']}")



