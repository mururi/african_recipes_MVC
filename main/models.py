from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    prep_time = models.IntegerField()
    posted_by = models.CharField(max_length=50)
    serves = models.IntegerField()
    ingredients = models.TextField()
    process = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def create_recipe(self):
        '''
        Method to create/save a Recipe object
        '''
        self.save()

    @classmethod
    def get_recipes(cls):
        '''
        Method to get all Recipe objects
        '''
        recipes = cls.objects.all()
        return recipes

    @classmethod
    def delete_recipe(cls, id):
        '''
        Method to delete a Recipe object
        '''
        cls.objects.filter(id = id).delete()