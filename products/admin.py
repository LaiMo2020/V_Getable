from django.contrib import admin
from .models import Product, Category
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
        'unit',
        'image',
    )

    ordering = ('name', )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)


