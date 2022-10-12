from email.policy import default
from wsgiref.validate import validator
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Pokemon(models.Model):

    class PokemonType(models.TextChoices):
        WATER = 'WA'
        GRASS = 'GR'
        GHOST = 'GH'
        STEEL = 'ST'
        FAIRY = 'FA'


    name = models.CharField(max_length=30)
    type = models.CharField(max_length=100,choices=PokemonType.choices)
    hp = models.PositiveIntegerField(validators = [MinValueValidator(50),MaxValueValidator(350)])
    active = models.BooleanField(default=True)
    name_fr = models.CharField(max_length=30, default="", blank = True)
    name_ar = models.CharField(max_length=30, default="", blank = True)
    name_jp = models.CharField(max_length=30, default="", blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
