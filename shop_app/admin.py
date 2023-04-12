from django.contrib import admin

# Register your models here.
from shop_app.models import ReviewRating, Location, CarReview


class RatingAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
        'image',
        'review',
        'rating',
        'created_at',


    )
#     # This will help you to disbale add functionality
#     def has_add_permission(self, request):
#         return False
#
#         # This will help you to disable delete functionaliyt
#
#     def has_delete_permission(self, request, obj=None):
#         return False
#
#         # This will help you to disable change functionality
#
#     def has_change_permission(self, request, obj=None):
#         return False

admin.site.register(ReviewRating, RatingAdmin)


class CarRatingAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
        'image',
        'review',
        'rating',
        'created_at',


    )
#     # This will help you to disbale add functionality
#     def has_add_permission(self, request):
#         return False
#
#         # This will help you to disable delete functionaliyt
#
#     def has_delete_permission(self, request, obj=None):
#         return False
#
#         # This will help you to disable change functionality
#
#     def has_change_permission(self, request, obj=None):
#         return False

admin.site.register(CarReview, CarRatingAdmin)
#
admin.site.register(Location)