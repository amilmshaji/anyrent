# Generated by Django 4.1.7 on 2023-04-18 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_rename_house_type_house_product_type_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0002_payment_orderplaced'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderPlacedCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('status', models.CharField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='New', max_length=10)),
                ('is_ordered', models.BooleanField(default=False)),
                ('ordered_date', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.payment')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.car_product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Order Details',
                'verbose_name_plural': 'Order Details',
            },
        ),
    ]
