# Create your tests here.
from django.test import TestCase
from .models import Recipe

class RecipeModelTest(TestCase):

    def test_recipe_creation(self):
        recipe = Recipe.objects.create(title="Test Recipe", description="A test recipe.", cooking_time=45)
        self.assertEqual(recipe.title, "Test Recipe")
        self.assertEqual(recipe.description, "A test recipe.")
        self.assertEqual(recipe.cooking_time, 45)

    def test_string_representation(self):
        recipe = Recipe.objects.create(title="Pasta", description="Delicious pasta recipe", cooking_time=20)
        self.assertEqual(str(recipe), "Pasta")

    def test_recipe_has_ingredients(self):
        recipe = Recipe.objects.create(title="Pancakes", description="Fluffy pancakes", cooking_time=15)
        self.assertEqual(recipe.ingredients.count(), 0)
