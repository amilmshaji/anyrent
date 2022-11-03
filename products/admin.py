from django.contrib import admin
# import admin_thumbnails


# Register your models here.

from .models import House_Product, Car_Product, Bike_Product, Other_Product,Furn_Product,Category


admin.site.register(Category)

admin.site.register(Car_Product)
admin.site.register(Bike_Product)
admin.site.register(Furn_Product)
admin.site.register(Other_Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'ad_title',
        'rent',
        'type',
        'furnish',
        'thumbnail_preview',
        'bedroom',
        'bathroom',
        'category',
        'created_date',
        'is_available',
    )
    prepopulated_fields = {'slug': ('ad_title',)}

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview
    thumbnail_preview.short_description = 'Image Preview'
    thumbnail_preview.allow_tags = True

admin.site.register(House_Product,ProductAdmin)

