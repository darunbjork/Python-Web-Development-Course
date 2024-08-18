# Create your tests here.
from django.test import TestCase
from .models import Recipe
from categories.models import Category

class RecipeModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Dessert")
        self.recipe = Recipe.objects.create(
            name="Chocolate Cake",
            description="Delicious chocolate cake",
            cooking_time=60,
            difficulty="Easy",
            category=self.category
        )

    def test_recipe_creation(self):
        self.assertEqual(self.recipe.name, "Chocolate Cake")
        self.assertEqual(self.recipe.cooking_time, 60)
        self.assertEqual(self.recipe.category.name, "Dessert")
