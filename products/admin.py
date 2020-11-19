from django.contrib import admin
from .models import Product, Category
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
            ('Vegetable', 'Vegetable'),
            ('Fruits', 'Fruits'),
        )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
        'unit',
        'image',
    )


admin.site.register(Product)
admin.site.register(Category)


