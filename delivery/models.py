from django.db import models
from cloudinary.models import CloudinaryField

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('Category', related_name='item')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
