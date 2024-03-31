from django.db import models

# Create your models here.
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Color(models.Model):
    color = models.CharField(max_length=255)

    def __str__(self):
        return self.color


class Car(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cars/')

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"
