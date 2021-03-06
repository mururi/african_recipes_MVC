from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-recipe/', views.add_recipe, name='add-recipe'),
    path('recipe/<int:pk>/', views.view_recipe, name='view-recipe'),
    path('update-recipe/<int:pk>/', views.update_recipe, name='update-recipe'),
    path('delete-recipe/<int:pk>/', views.delete_recipe, name='delete-recipe'),
]