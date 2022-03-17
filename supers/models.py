from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User






# Create your models here.


class super(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    primary_ability = models.CharField(max_length=255)
    second_ability = models.CharField(max_length=255)
    catchphrase = models.CharField(max_length=255)
    super_type = models.ForeignKey(User, on_delete=models.CASCADE)
