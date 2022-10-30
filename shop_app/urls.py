from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.shop, name='shop'),
    path('category/<slug:category_slug>/<slug:product_slug>/',
         views.product_detail, name='product_detail'),
    # path('category/<slug:category_slug>/<slug:product_slug>/',
    #      views.car_detail, name='car_detail'),


]