import pickle

def calc_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        return 'Easy'
    elif cooking_time < 10 and len(ingredients) >= 4:
        return 'Medium'
    elif cooking_time >= 10 and len(ingredients) < 4:
        return 'Intermediate'
    else:
        return 'Hard'

def take_recipe():
    name = input("Enter the name of the recipe: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = input("Enter the ingredients (comma-separated): ").split(', ')
    difficulty = calc_difficulty(cooking_time, ingredients)
    return {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients,
        'difficulty': difficulty
    }

filename = input("Enter the filename to save recipes: ")

try:
    with open(filename, 'rb') as file:
        data = pickle.load(file)
except FileNotFoundError:
    data = {'recipes_list': [], 'all_ingredients': []}
except Exception as e:
    print(f"An error occurred: {e}")
    data = {'recipes_list': [], 'all_ingredients': []}

recipes_list = data['recipes_list']
all_ingredients = data['all_ingredients']

num_recipes = int(input("How many recipes would you like to enter? "))
for _ in range(num_recipes):
    recipe = take_recipe()
    recipes_list.append(recipe)
    for ingredient in recipe['ingredients']:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)

data = {'recipes_list': recipes_list, 'all_ingredients': all_ingredients}

with open(filename, 'wb') as file:
    pickle.dump(data, file)
