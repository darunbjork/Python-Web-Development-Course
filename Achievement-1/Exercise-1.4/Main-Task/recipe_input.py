# recipe_input.py
import pickle

def calc_difficulty(cooking_time, num_ingredients):
    if cooking_time < 10:
        if num_ingredients < 4:
            return 'Easy'
        else:
            return 'Medium'
    else:
        if num_ingredients < 4:
            return 'Intermediate'
        else:
            return 'Hard'

def take_recipe():
    name = input("Enter the recipe name: ")
    cooking_time = int(input("Enter the cooking time in minutes: "))
    ingredients = input("Enter the ingredients (comma separated): ").split(',')
    ingredients = [ingredient.strip() for ingredient in ingredients]
    difficulty = calc_difficulty(cooking_time, len(ingredients))
    return {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients, 'difficulty': difficulty}

filename = input("Enter the filename to store recipes: ")

try:
    with open(filename, 'rb') as file:
        data = pickle.load(file)
except FileNotFoundError:
    data = {'recipes_list': [], 'all_ingredients': []}
except:
    data = {'recipes_list': [], 'all_ingredients': []}
finally:
    recipes_list = data.get('recipes_list', [])
    all_ingredients = data.get('all_ingredients', [])

num_recipes = int(input("How many recipes would you like to enter? "))

for _ in range(num_recipes):
    recipe = take_recipe()
    recipes_list.append(recipe)
    for ingredient in recipe['ingredients']:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)

data['recipes_list'] = recipes_list
data['all_ingredients'] = all_ingredients

with open(filename, 'wb') as file:
    pickle.dump(data, file)

