# # from carts.views import cart
# from django.db import models
#
# from products.models import House_Product
# from accounts.models import Account
#
#
# # Create your models here.
#
#
# class Wishlist(models.Model):
#     wishlist_id = models.CharField(max_length=250, blank=True)
#     date_added = models.DateField(auto_now_add=True)
#
#     def __str__(self):
#         return self.wishlist_id
#
#
# class WishlistItem(models.Model):
#     user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
#     house_product = models.ForeignKey(House_Product, on_delete=models.CASCADE,null=True)
#     wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, null=True)
#     quantity = models.IntegerField()
#     is_active = models.BooleanField(default=True)
#
#     def sub_total(self):
#         return self.house_product.price*self.quantity
#
#     def __unicode__(self):
#         return self.house_product