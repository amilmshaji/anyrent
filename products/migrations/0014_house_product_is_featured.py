# Generated by Django 4.1.7 on 2023-03-08 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_house_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='house_product',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
