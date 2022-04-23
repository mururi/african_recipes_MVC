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