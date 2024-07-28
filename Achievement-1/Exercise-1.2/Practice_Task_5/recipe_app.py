recipe_1 = {
    "name": "Tea",
    "cooking_time": 5,
    "ingredients": ["Tea leaves", "Sugar", "Water"]
}
all_recipes = [recipe_1]

recipe_2 = {"name": "Coffee", "cooking_time": 5, "ingredients": ["Coffee beans", "Sugar", "Water"]}
recipe_3 = {"name": "Pasta", "cooking_time": 20, "ingredients": ["Pasta", "Tomato sauce", "Salt"]}
recipe_4 = {"name": "Omelette", "cooking_time": 10, "ingredients": ["Eggs", "Salt", "Pepper", "Oil"]}
recipe_5 = {"name": "Salad", "cooking_time": 10, "ingredients": ["Lettuce", "Tomato", "Cucumber", "Dressing"]}

all_recipes.extend([recipe_2, recipe_3, recipe_4, recipe_5])

for recipe in all_recipes:
    print(f"Ingredients for {recipe['name']}: {recipe['ingredients']}")

