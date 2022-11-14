# Generated by Django 4.1.3 on 2022-11-14 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(editable=False, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='fname',
            field=models.CharField(blank=True, editable=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='lname',
            field=models.CharField(blank=True, editable=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.BigIntegerField(default=0, editable=False),
        ),
    ]
