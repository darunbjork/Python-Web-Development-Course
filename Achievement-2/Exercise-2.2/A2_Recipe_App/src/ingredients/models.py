# Create your models here.
from django.db import models
from recipes.models import Recipe

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quantity} of {self.name} for {self.recipe.title}"
