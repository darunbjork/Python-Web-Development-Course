from django.shortcuts import render
from django.views.generic import DetailView
from .models import Recipe

# Home page view
def home_view(request):
    return render(request, 'recipes/home.html')

# Recipes list view
def recipes_home(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
