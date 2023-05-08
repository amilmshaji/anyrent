from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('home/', views.Home, name='home'),

    path('shop/', views.shop, name='shop'),
    path('SHOP/', views.shop, name='SHOP'),

    path('category/<slug:category_slug>/<slug:product_slug>/',
         views.product_detail, name='product_detail'),
    path('category/<slug:category_slug>/',
         views.shop, name='products_by_category'),
    path('search/', views.search, name='search'),
    path('search-suggestions/', views.search_suggestions, name='search_suggestions'),

    path('location_search/', views.location_search, name='location_search'),

    path('submit_review/<int:product_id>/',views.House_review, name='submit_review'),
    path('review_car/<int:product_id>/',views.Car_review, name='review_car'),
    path('review_bike/<int:product_id>/', views.Bike_review, name='review_bike'),
    path('review_furn/<int:product_id>/', views.Furn_review, name='review_furn'),
    path('review_other/<int:product_id>/', views.Other_review, name='review_other'),

    path('map/', views.map_view, name='map'),
    path('prod_map/<str:location>/', views.prod_map_view, name='prod_map'),

]
