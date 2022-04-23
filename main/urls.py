from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-recipe', views.add_recipe, name='add-recipe')
]