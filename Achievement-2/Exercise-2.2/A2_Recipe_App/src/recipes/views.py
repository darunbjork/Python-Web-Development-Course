from django.shortcuts import render
from django.views.generic import DetailView
from .models import Recipe
from .forms import RecipeSearchForm
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# Set matplotlib to use the 'Agg' backend (no GUI required)
plt.switch_backend('Agg')

# Home page view
def home_view(request):
    return render(request, 'recipes/home.html')

# Recipes list view with search and chart functionality
def recipes_home(request):
    form = RecipeSearchForm(request.POST or None)
    recipes = Recipe.objects.all()
    chart = None

    if request.method == 'POST' and form.is_valid():
        recipe_title = form.cleaned_data.get('recipe_title')
        chart_type = form.cleaned_data.get('chart_type')

        # Filter recipes by title if provided
        if recipe_title:
            recipes = recipes.filter(title__icontains=recipe_title)

        # Convert to DataFrame for data analysis
        recipes_df = pd.DataFrame(list(recipes.values('title', 'cooking_time', 'difficulty')))

        if not recipes_df.empty:
            chart = generate_chart(recipes_df, chart_type)

    return render(request, 'recipes/recipe_list.html', {'recipes': recipes, 'form': form, 'chart': chart})

# Recipe detail view
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'

# Generate chart using matplotlib
def generate_chart(data, chart_type):
    fig, ax = plt.subplots()

    if chart_type == 'Bar':
        data.groupby('title').size().plot(kind='bar', ax=ax)
    elif chart_type == 'Pie':
        data.groupby('title').size().plot(kind='pie', autopct='%1.1f%%', ax=ax)
    elif chart_type == 'Line':
        data.groupby('title').size().plot(kind='line', ax=ax)

    ax.set_title(f'{chart_type} Chart of Recipes')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    chart = base64.b64encode(image_png).decode('utf-8')
    return chart
