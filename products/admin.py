from django.contrib import admin

# Register your models here.

from .models import House_Product, Car_Product, Bike_Product, Other_Product,Furn_Product,Category,All_Products


admin.site.register(Category)

admin.site.register(House_Product)
admin.site.register(Car_Product)
admin.site.register(Bike_Product)
admin.site.register(Furn_Product)
admin.site.register(Other_Product)
admin.site.register(All_Products)