# Create your models here.
from django.db import models
from categories.models import Category

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    cooking_time = models.IntegerField(help_text="Time in minutes")
    difficulty = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
