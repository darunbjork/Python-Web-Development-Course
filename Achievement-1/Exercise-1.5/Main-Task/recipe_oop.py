class Recipe:
    all_ingredients = []

    def __init__(self, name, cooking_time):
        self.name = name
        self.cooking_time = cooking_time
        self.ingredients = []
        self.difficulty = None

    def add_ingredients(self, *args):
        self.ingredients.extend(args)
        self.update_all_ingredients()

    def get_ingredients(self):
        return self.ingredients

    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            self.difficulty = 'Easy'
        elif self.cooking_time < 10:
            self.difficulty = 'Medium'
        elif len(self.ingredients) < 4:
            self.difficulty = 'Intermediate'
        else:
            self.difficulty = 'Hard'

    def get_difficulty(self):
        if not self.difficulty:
            self.calculate_difficulty()
        return self.difficulty

    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients

    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in Recipe.all_ingredients:
                Recipe.all_ingredients.append(ingredient)

    def __str__(self):
        return f"Recipe: {self.name}\nCooking time: {self.cooking_time} minutes\nIngredients: {', '.join(self.ingredients)}\nDifficulty: {self.get_difficulty()}"

def recipe_search(data, search_term):
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)

tea = Recipe("Tea", 5)
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
print(tea)

coffee = Recipe("Coffee", 5)
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
print(coffee)

cake = Recipe("Cake", 50)
cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")
print(cake)

smoothie = Recipe("Banana Smoothie", 5)
smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
print(smoothie)

recipes_list = [tea, coffee, cake, smoothie]

print("\nRecipes with 'Water':")
recipe_search(recipes_list, "Water")

print("\nRecipes with 'Sugar':")
recipe_search(recipes_list, "Sugar")

print("\nRecipes with 'Bananas':")
recipe_search(recipes_list, "Bananas")

