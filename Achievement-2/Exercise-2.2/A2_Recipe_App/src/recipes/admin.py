from django.contrib import admin
from .models import Recipe
from ingredients.models import Ingredient

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1  # This lets you add one additional blank ingredient by default.

class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline]

admin.site.register(Recipe, RecipeAdmin)
