# Generated by Django 4.1.3 on 2022-11-23 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_bike_product_ad_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike_product',
            name='add_info',
            field=models.TextField(blank=True, editable=False, max_length=500, null=True),
        ),
    ]
