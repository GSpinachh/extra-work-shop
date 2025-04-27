from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    rating = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    description = models.TextField(max_length=700, blank=True)
    characteristics = models.TextField(max_length=700, blank=True)
    image = models.ImageField(upload_to="static/medias", blank=True, null=True)

    def __str__(self):
        return self.name