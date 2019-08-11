from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Movie(models.Model):  # 1
    title = models.CharField(max_length=128)
    imdb = models.FloatField(validators=[MaxValueValidator(10.0),MinValueValidator(0.0)])  # 2

    def __str__(self):
        return self.title  # 3
