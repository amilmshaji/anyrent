# Generated by Django 4.1.7 on 2023-04-18 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_house_product_is_featured'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house_product',
            old_name='type',
            new_name='house_type',
        ),
    ]
