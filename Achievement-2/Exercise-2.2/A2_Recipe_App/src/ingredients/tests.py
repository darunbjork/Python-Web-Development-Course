# Create your tests here.
from django.test import TestCase
from .models import Ingredient
from recipes.models import Recipe
from categories.models import Category

class IngredientModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Dessert")
        self.recipe = Recipe.objects.create(
            name="Chocolate Cake",
            description="Delicious chocolate cake",
            cooking_time=60,
            difficulty="Easy",
            category=self.category
        )
        self.ingredient = Ingredient.objects.create(
            name="Chocolate",
            quantity="200g",
            recipe=self.recipe
        )

    def test_ingredient_creation(self):
        self.assertEqual(self.ingredient.name, "Chocolate")
        self.assertEqual(self.ingredient.quantity, "200g")
        self.assertEqual(self.ingredient.recipe.name, "Chocolate Cake")
