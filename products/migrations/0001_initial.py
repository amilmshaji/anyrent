# Generated by Django 4.1.1 on 2022-10-10 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('cat_image', models.ImageField(blank=True, upload_to='photos/categories')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Other_Product',
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
                ('category', models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='House_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(editable=False, max_length=200, unique=True)),
                ('add_info', models.TextField(blank=True, max_length=500)),
                ('rent', models.IntegerField()),
                ('bedroom', models.IntegerField()),
                ('bathroom', models.IntegerField()),
                ('builtup', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('type', models.CharField(blank=True, max_length=200)),
                ('furnish', models.CharField(blank=True, max_length=200)),
                ('images', models.ImageField(upload_to='photos/house')),
                ('is_available', models.BooleanField(default=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
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
                ('category', models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='Car_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(editable=False, max_length=200, unique=True)),
                ('add_info', models.TextField(blank=True, max_length=500)),
                ('rent', models.IntegerField()),
                ('brand', models.CharField(blank=True, max_length=200)),
                ('driven', models.IntegerField()),
                ('own', models.CharField(blank=True, max_length=200)),
                ('fuel', models.CharField(blank=True, max_length=200)),
                ('images', models.ImageField(upload_to='photos/house')),
                ('is_available', models.BooleanField(default=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='Bike_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(editable=False, max_length=200, unique=True)),
                ('add_info', models.TextField(blank=True, max_length=500)),
                ('rent', models.IntegerField()),
                ('brand', models.CharField(blank=True, max_length=200)),
                ('driven', models.IntegerField()),
                ('own', models.CharField(blank=True, max_length=200)),
                ('images', models.ImageField(upload_to='photos/house')),
                ('is_available', models.BooleanField(default=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
    ]
