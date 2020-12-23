from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Product(models.Model):

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL, related_name='products')
    name = models.CharField(max_length=254, default='')
    description = models.CharField(max_length=254, default='')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.CharField(max_length=254, default='')
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
