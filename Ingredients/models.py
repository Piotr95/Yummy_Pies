from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Ingredients(models.Model):
    name = models.CharField(max_length=250)
    pics = models.ImageField(default='', upload_to="ingridiants_pics")


    def __str__(self):
        return self.name
