from django.db import models

from django.contrib.auth.models import User

class Product(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    division=models.CharField(max_length=10)
    class Meta:
        ordering=['-id']
