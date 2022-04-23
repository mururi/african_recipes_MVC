from django.db import models
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField

class Recipe(models.Model):
    image = CloudinaryField('image')
    title = models.CharField(max_length=50)
    description = HTMLField()
    prep_time = models.IntegerField()
    posted_by = models.CharField(max_length=50)
    serves = models.IntegerField()
    ingredients = HTMLField()
    process = HTMLField()
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
        return cls.objects.all()

    @classmethod
    def get_recipe_by_id(cls, id):
        '''
        Method to get a recipe by its ID
        '''
        return cls.objects.filter(id = id)[0]

    @classmethod
    def delete_recipe(cls, id):
        '''
        Method to delete a Recipe object
        '''
        cls.objects.filter(id = id).delete()