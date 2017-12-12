from django.db import models
from django.conf import settings

# Create your models here.
class 


class Category (models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
