# Generated by Django 4.1.1 on 2022-10-10 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_all_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='all_products',
            old_name='cart_id',
            new_name='proudct_id',
        ),
    ]
