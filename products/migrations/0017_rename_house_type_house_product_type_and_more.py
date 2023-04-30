# Generated by Django 4.1.7 on 2023-04-18 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_house_product_payment_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house_product',
            old_name='house_type',
            new_name='type',
        ),
        migrations.AddField(
            model_name='bike_product',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='car_product',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='furn_product',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='other_product',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
    ]