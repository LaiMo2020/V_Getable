# Generated by Django 3.1.3 on 2020-11-20 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201119_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(default='', max_length=254),
        ),
    ]