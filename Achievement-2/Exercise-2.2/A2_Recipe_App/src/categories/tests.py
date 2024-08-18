# Create your tests here.
from django.test import TestCase
from .models import Category

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Dessert")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Dessert")
