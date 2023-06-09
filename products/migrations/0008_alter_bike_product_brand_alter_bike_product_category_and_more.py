# Generated by Django 4.1.3 on 2022-11-23 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_bike_product_add_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike_product',
            name='brand',
            field=models.CharField(blank=True, editable=False, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='bike_product',
            name='category',
            field=models.ForeignKey(default=3, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category'),
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
