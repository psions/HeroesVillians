from django.db import models
from django.forms import CharField


# Create your models here.

class super_type(models.Model):
    type = CharField(max_length=255)