from django.shortcuts import render, redirect
from main.models import Recipe
from .forms import RecipeForm

def home(request):
    recipes = Recipe.get_recipes()

    context = {
        "recipes": recipes
    }
    return render(request, 'index.html', context)

def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = RecipeForm()

    context = {
        "form": form
    }
    return render(request, 'add-recipe.html', context)

def view_recipe(request, pk):
    recipe = Recipe.get_recipe_by_id(pk)

    context = {
        "recipe": recipe
    }
    return render(request, 'view-recipe.html', context)
