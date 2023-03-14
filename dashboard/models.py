from django.db import models

# Create your models here.
from products.models import House_Product


class Productgallery(models.Model):
    product=models.ForeignKey(House_Product, default=None, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='store/products', max_length=255)

    def __str__(self):
        return self.product.ad_title

    class Meta:
        verbose_name='Product Gallery'
        verbose_name_plural='Product gallery'