
# Create your views here.
from django.shortcuts import render

def recipes_home(request):
    return render(request, 'recipes/home.html')
