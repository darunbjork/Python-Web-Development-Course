import pickle

# Step 4: Load the recipe data from the binary file
with open('../1.4-Practice Task 2/recipe_binary.bin', 'rb') as file:
    loaded_recipe = pickle.load(file)

print("Recipe details:")
print(f"Name: {loaded_recipe['name']}")
print(f"Ingredients: {', '.join(loaded_recipe['ingredients'])}")
print(f"Cooking Time: {loaded_recipe['cooking_time']} minutes")
print(f"Difficulty: {loaded_recipe['difficulty']}")


