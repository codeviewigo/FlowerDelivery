from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/products/')
    short_description = models.TextField(max_length=500, default='')
    full_description = models.TextField(default='')
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
