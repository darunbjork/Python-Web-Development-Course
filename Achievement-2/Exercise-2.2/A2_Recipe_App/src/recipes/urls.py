from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Home page with welcome message
    path('recipes/', views.recipes_home, name='recipes_home'),  # Recipes list page
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe_detail'),  # Recipe detail page
]
