from django.test import TestCase
from .models import Recipe
from datetime import datetime

class RecipeTestClass(TestCase):
    '''
    Test class to test the behavior of the Recipe model class
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''
        self.new_recipe = Recipe(title = 'Test Title', description = 'Test description', prep_time = 120, posted_by = 'John Doe', serves = 3, ingredients = 'List of ingredients', process = 'Test Process', date_posted = datetime.now())
        self.new_recipe.save()

    def test_instance(self):
        '''
        Method to test if the new_recipe object is an instance of the Recipe model
        '''
        self.assertTrue(isinstance(self.new_recipe, Recipe))

    def test_get_recipes(self):
        '''
        Method to test the get_recipes method
        '''
        recipes = Recipe.get_recipes()
        self.assertTrue(len(recipes) > 0)

    def test_delete(self):
        '''
        Method to test the delete_recipe method
        '''
        Recipe.delete_recipe(self.new_recipe.id)
        recipes = Recipe.objects.all()
        self.assertTrue(len(recipes) == 0)
