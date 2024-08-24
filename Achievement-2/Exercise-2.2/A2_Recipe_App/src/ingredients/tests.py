# Create your tests here.
from django.test import TestCase
from .models import Ingredient
from recipes.models import Recipe

class IngredientModelTest(TestCase):

    def test_ingredient_creation(self):
        recipe = Recipe.objects.create(title="Pancakes", description="Fluffy pancakes", cooking_time=15)
        ingredient = Ingredient.objects.create(name="Flour", quantity="2 cups", recipe=recipe)
        self.assertEqual(ingredient.name, "Flour")
        self.assertEqual(ingredient.quantity, "2 cups")
        self.assertEqual(ingredient.recipe.title, "Pancakes")

    def test_string_representation(self):
        recipe = Recipe.objects.create(title="Pancakes", description="Fluffy pancakes", cooking_time=15)
        ingredient = Ingredient.objects.create(name="Sugar", quantity="1 cup", recipe=recipe)
        self.assertEqual(str(ingredient), "1 cup of Sugar for Pancakes")
