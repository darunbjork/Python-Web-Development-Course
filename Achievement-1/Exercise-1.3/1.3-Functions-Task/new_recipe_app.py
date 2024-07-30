# new_recipe_app.py
def take_recipe():
    name = input("Enter the name of the recipe: ")
    cooking_time = int(input("Enter the cooking time in minutes: "))
    ingredients = input("Enter the ingredients separated by commas: ").split(", ")
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients
    }
    return recipe

recipes_list = []
ingredients_list = []

n = int(input("How many recipes would you like to enter? "))

for _ in range(n):
    recipe = take_recipe()
    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)

for recipe in recipes_list:
    name = recipe['name']
    cooking_time = recipe['cooking_time']
    ingredients = recipe['ingredients']
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = "Easy"
    elif cooking_time < 20 and len(ingredients) >= 4:
        difficulty = "Medium"
    else:
        difficulty = "Hard"
    print(f"Recipe: {name}\nCooking time: {cooking_time} minutes\nIngredients: {', '.join(ingredients)}\nDifficulty: {difficulty}\n")

print("All ingredients: ", ", ".join(sorted(ingredients_list)))
