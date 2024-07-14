from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=255)
    recipe_details = models.TextField()

    def __str__(self):
        return self.recipe_name