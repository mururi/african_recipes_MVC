from django.shortcuts import render, redirect
from main.models import Recipe
from .forms import RecipeForm
from django.urls import reverse
from django.contrib import messages

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
            messages.success(request, "New Recipe Has Been Added Successfuly.")
        return redirect('home')
    else:
        form = RecipeForm()

    context = {
        "form": form
    }
    return render(request, 'create-recipe.html', context)

def view_recipe(request, pk):
    recipe = Recipe.get_recipe_by_id(pk)

    context = {
        "recipe": recipe
    }
    return render(request, 'view-recipe.html', context)

def update_recipe(request, pk):
    recipe = Recipe.objects.get(id = pk)
    form = RecipeForm(instance=recipe)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, "Recipe Has Been Edited Successfuly.")
        return redirect(reverse('view-recipe', args=[recipe.id]))
    
    context = {
        "form": form,
        "recipe": recipe
    }
    return render(request, 'update-recipe.html', context)

def delete_recipe(request, pk):
    recipe = Recipe.objects.get(id = pk)
    if request.method == 'POST':
        recipe.delete()
        messages.warning(request, "Recipe Has Been Deleted.")
        return redirect('home')

    context = {
        "recipe": recipe
    }
    return render(request, 'delete-recipe.html', context)