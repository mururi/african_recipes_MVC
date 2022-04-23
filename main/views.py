from django.shortcuts import render

from main.models import Recipe

def home(request):
    recipes = Recipe.get_recipes()

    context = {
        "recipes": recipes
    }
    return render(request, 'index.html', context)