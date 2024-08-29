# Register your models here.
from django.contrib import admin
from .models import Recipe
from ingredients.models import Ingredient

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1  # Number of extra empty forms to display

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline]  # Attach the Ingredient model inline to the Recipe admin
    list_display = ('title', 'cooking_time', 'difficulty', 'category')
    search_fields = ('title', 'description')
    list_filter = ('category', 'difficulty', 'cooking_time')

