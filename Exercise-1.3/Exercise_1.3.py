# Exercise_1.3.py

# Initialize lists
recipes_list = []  # Empty list to store recipe dictionaries
ingredients_list = []  # Empty list to store unique ingredients

# Function to take recipe input from the user
def take_recipe():
  """
  This function prompts the user for recipe details and returns a dictionary containing the information.
  """
  name = input("Enter the name of the recipe: ")
  cooking_time = int(input("Enter the cooking time (in minutes): "))
  ingredients = input("Enter the ingredients (comma-separated): ").split(',')
  recipe = {
      'name': name,
      'cooking_time': cooking_time,
      'ingredients': [ingredient.strip() for ingredient in ingredients]  # Remove leading/trailing whitespaces from ingredients
  }
  return recipe

# Main code
n = int(input("How many recipes would you like to enter? "))

for _ in range(n):
  recipe = take_recipe()
  for ingredient in recipe['ingredients']:
    if ingredient not in ingredients_list:  # Check if ingredient is already in the list
      ingredients_list.append(ingredient)
  recipes_list.append(recipe)

for recipe in recipes_list:
  # Determine recipe difficulty based on cooking time and number of ingredients
  if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
    difficulty = 'Easy'
  elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
    difficulty = 'Medium'
  elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
    difficulty = 'Intermediate'
  else:
    difficulty = 'Hard'

  # Print recipe details
  print(f"Recipe: {recipe['name']}")
  print(f"Cooking Time: {recipe['cooking_time']} minutes")
  print(f"Ingredients: {', '.join(recipe['ingredients'])}")
  print(f"Difficulty: {difficulty}")
  print()

# Sort ingredients list alphabetically
ingredients_list.sort()

# Print the list of unique ingredients
print("Ingredients List:")
for ingredient in ingredients_list:
  print(ingredient)
