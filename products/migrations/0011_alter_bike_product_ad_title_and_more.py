# Generated by Django 4.1.5 on 2023-02-27 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_car_product_ad_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike_product',
            name='ad_title',
            field=models.CharField(editable=False, max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='bike_product',
            name='add_info',
            field=models.TextField(blank=True, editable=False, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='bike_product',
            name='brand',
            field=models.CharField(blank=True, editable=False, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='bike_product',
            name='driven',
            field=models.IntegerField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='bike_product',
            name='images',
            field=models.ImageField(editable=False, null=True, upload_to='photos/house'),
        ),
        migrations.AlterField(
            model_name='bike_product',
            name='own',
            field=models.CharField(blank=True, editable=False, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='bike_product',
            name='rent',
            field=models.IntegerField(editable=False, null=True),
        ),
    ]
