from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),

    path('shop/', views.shop, name='shop'),
    path('category/<slug:category_slug>/<slug:product_slug>/',
         views.product_detail, name='product_detail'),
    path('category/<slug:category_slug>/',
         views.shop, name='products_by_category'),
    path('search/', views.search, name='search'),
    path('location_search/', views.location_search, name='location_search'),

    path('submit_review/<int:product_id>/',
         views.submit_review, name='submit_review'),

    path('map/', views.map_view, name='map'),
    path('prod_map/<str:location>/', views.prod_map_view, name='prod_map'),

]