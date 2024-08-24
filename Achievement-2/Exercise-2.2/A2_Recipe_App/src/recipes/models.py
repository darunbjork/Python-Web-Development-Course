# Create your models here.
from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    cooking_time = models.IntegerField(help_text="Time in minutes")
    instructions = models.TextField(default="No instructions provided")
    difficulty = models.CharField(max_length=50, choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')])
    category = models.CharField(max_length=100, choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Dessert', 'Dessert'), ('Salad', 'Salad')])

    def __str__(self):
        return self.title

   

    
