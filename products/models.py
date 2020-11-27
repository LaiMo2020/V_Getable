from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Product(models.Model):

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254, default='')
    description = models.CharField(max_length=254, default='')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.CharField(max_length=254, default='')
    image_url = models.URLField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
