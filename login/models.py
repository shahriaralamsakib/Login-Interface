from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class MyModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Other fields for your model
