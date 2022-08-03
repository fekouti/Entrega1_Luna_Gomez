from pyexpat import model
from django.db import models

# Create your models here.

def __str__(self):
    return self.name


class Users(models.Model):
    name = models.CharField(max_length=40)
    job = models.CharField(max_length=60)
    email = models.CharField(max_length=35)
    password = models.CharField(max_length=12)


class Posts(models.Model):
    title = models.CharField(max_length=140)
    subtitle = models.CharField(max_length=240)
    postContent = models.CharField(max_length=50000)
