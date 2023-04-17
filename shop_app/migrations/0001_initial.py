# Generated by Django 4.1.7 on 2023-04-17 05:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0014_house_product_is_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('images', models.ImageField(null=True, upload_to='photos/loc')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(blank=True, max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/house')),
                ('rating', models.FloatField()),
                ('ip', models.CharField(blank=True, editable=False, max_length=20)),
                ('status', models.BooleanField(default=True, editable=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('product', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='products.house_product')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OtherReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(blank=True, max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/house')),
                ('rating', models.FloatField()),
                ('ip', models.CharField(blank=True, editable=False, max_length=20)),
                ('status', models.BooleanField(default=True, editable=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('product', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='products.other_product')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FurnReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(blank=True, max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/house')),
                ('rating', models.FloatField()),
                ('ip', models.CharField(blank=True, editable=False, max_length=20)),
                ('status', models.BooleanField(default=True, editable=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('product', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='products.furn_product')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CarReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(blank=True, max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/house')),
                ('rating', models.FloatField()),
                ('ip', models.CharField(blank=True, editable=False, max_length=20)),
                ('status', models.BooleanField(default=True, editable=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('product', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='products.car_product')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BikeReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(blank=True, max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/house')),
                ('rating', models.FloatField()),
                ('ip', models.CharField(blank=True, editable=False, max_length=20)),
                ('status', models.BooleanField(default=True, editable=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('product', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='products.bike_product')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
