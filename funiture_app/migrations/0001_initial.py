# Generated by Django 4.1.1 on 2022-10-05 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Furn_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(editable=False, max_length=200, unique=True)),
                ('add_info', models.TextField(blank=True, max_length=500)),
                ('rent', models.IntegerField()),
                ('images', models.ImageField(upload_to='photos/house')),
                ('is_available', models.BooleanField(default=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('type', models.CharField(blank=True, max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='shop_app.category')),
            ],
        ),
    ]
