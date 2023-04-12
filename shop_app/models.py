from django.db import models
from django.utils.html import mark_safe



from django.urls.base import reverse

from accounts.models import Account
from products.models import House_Product, Car_Product, Bike_Product, Furn_Product, Other_Product


class ReviewRating(models.Model):
    product = models.ForeignKey(House_Product, on_delete=models.CASCADE,editable=False)
    user = models.ForeignKey(Account, on_delete=models.CASCADE,editable=False)
    review = models.TextField(max_length=500, blank=True,)
    image = models.ImageField(upload_to='photos/house',blank=True,null=True)

    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True,editable=False)
    status = models.BooleanField(default=True,editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.product)

class CarReview(models.Model):
    product = models.ForeignKey(Car_Product, on_delete=models.CASCADE,editable=False)
    user = models.ForeignKey(Account, on_delete=models.CASCADE,editable=False)
    review = models.TextField(max_length=500, blank=True,)
    image = models.ImageField(upload_to='photos/house',blank=True,null=True)

    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True,editable=False)
    status = models.BooleanField(default=True,editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.product)


class BikeReview(models.Model):
    product = models.ForeignKey(Bike_Product, on_delete=models.CASCADE,editable=False)
    user = models.ForeignKey(Account, on_delete=models.CASCADE,editable=False)
    review = models.TextField(max_length=500, blank=True,)
    image = models.ImageField(upload_to='photos/house',blank=True,null=True)

    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True,editable=False)
    status = models.BooleanField(default=True,editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.product)


class FurnReview(models.Model):
    product = models.ForeignKey(Furn_Product, on_delete=models.CASCADE,editable=False)
    user = models.ForeignKey(Account, on_delete=models.CASCADE,editable=False)
    review = models.TextField(max_length=500, blank=True,)
    image = models.ImageField(upload_to='photos/house',blank=True,null=True)

    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True,editable=False)
    status = models.BooleanField(default=True,editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.product)


class OtherReview(models.Model):
    product = models.ForeignKey(Other_Product, on_delete=models.CASCADE,editable=False)
    user = models.ForeignKey(Account, on_delete=models.CASCADE,editable=False)
    review = models.TextField(max_length=500, blank=True,)
    image = models.ImageField(upload_to='photos/house',blank=True,null=True)

    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True,editable=False)
    status = models.BooleanField(default=True,editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.product)


class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    images = models.ImageField(upload_to='photos/loc', null=True)

    def __str__(self):
        return self.name